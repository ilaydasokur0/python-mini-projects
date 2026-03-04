# main.py

from datetime import date
from typing import Optional

from services.library_service import LibraryService
from storage.json_storage import JsonStorage
from models.reading_entry import ReadingStatus


def ask(prompt: str) -> str:
    return input(prompt).strip()


def ask_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("Lütfen sayı gir.")


def ask_optional_date(prompt: str) -> Optional[date]:
    s = input(prompt).strip()
    if not s:
        return None
    try:
        y, m, d = s.split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        print("Tarih formatı yanlış. Boş bırak veya YYYY-MM-DD gir.")
        return None


def print_books(service: LibraryService):
    books = service.list_books()
    if not books:
        print("Katalog boş.")
        return
    print("\n--- Katalog ---")
    for b in books:
        print(f"{b.id} | {b.title} - {b.author}")


def print_my_library(service: LibraryService, user_id: str, status: Optional[ReadingStatus] = None):
    entries = service.list_user_entries(user_id, status=status)
    if not entries:
        print("Kütüphanen boş (bu filtrede sonuç yok).")
        return

    print("\n--- Benim Kütüphanem ---")
    for e in entries:
        book = service.get_book(e.book_id)
        sd = e.start_date.isoformat() if e.start_date else "-"
        ed = e.end_date.isoformat() if e.end_date else "-"
        rt = str(e.rating) if e.rating is not None else "-"
        print(f"{e.id} | [{e.status}] {book.title} - {book.author} | start:{sd} end:{ed} rating:{rt}")


def main():
    storage = JsonStorage("data/library_data.json")

    # JSON'dan yükle
    books, users, entries, reviews = storage.load()

    # Service oluştur ve RAM'e bas
    service = LibraryService()
    service.books = books
    service.users = users
    service.entries = entries
    service.reviews = reviews

    # Basit login: yoksa kullanıcı oluştur
    username = ask("Username: ")
    user = None
    for u in service.users.values():
        if u.username == username:
            user = u
            break

    if user is None:
        # Şimdilik password hash vs. yok; direkt string veriyoruz
        user = service.create_user(username=username, password_hash="dev")
        print(f"Yeni kullanıcı oluşturuldu: {user.username} ({user.id})")
    else:
        print(f"Hoş geldin: {user.username} ({user.id})")

    while True:
        print("\nMenu")
        print("1) Katalogu listele")
        print("2) Kitap ekle (kataloğa)")
        print("3) Kitabı kütüphaneme ekle (WANT)")
        print("4) Kütüphanemi listele")
        print("5) Filtre: WANT")
        print("6) Filtre: READING")
        print("7) Filtre: FINISHED")
        print("8) Okumaya başla (entry id ile)")
        print("9) Bitir + puan ver (entry id ile)")
        print("10) Yorum yaz (book id ile)")
        print("11) Kaydet & çık")

        choice = ask("Seçim: ")

        if choice == "1":
            print_books(service)

        elif choice == "2":
            title = ask("Title: ")
            author = ask("Author: ")
            b = service.add_book(title=title, author=author)
            print(f"Eklendi: {b.id} | {b.title}")

        elif choice == "3":
            print_books(service)
            book_id = ask("Kütüphanene eklemek istediğin book_id: ")
            try:
                e = service.add_to_library(user_id=user.id, book_id=book_id)
                print(f"Eklendi (entry): {e.id} | status={e.status}")
            except KeyError:
                print("Hatalı book_id veya user yok.")

        elif choice == "4":
            print_my_library(service, user.id)

        elif choice == "5":
            print_my_library(service, user.id, ReadingStatus.WANT)

        elif choice == "6":
            print_my_library(service, user.id, ReadingStatus.READING)

        elif choice == "7":
            print_my_library(service, user.id, ReadingStatus.FINISHED)

        elif choice == "8":
            entry_id = ask("Start için entry_id: ")
            d = ask_optional_date("Start date (YYYY-MM-DD) boş bırak = bugün: ")
            try:
                e = service.start_reading(entry_id, d)
                print(f"Güncellendi: {e.id} | status={e.status} | start={e.start_date}")
            except KeyError:
                print("Hatalı entry_id.")

        elif choice == "9":
            entry_id = ask("Finish için entry_id: ")
            d = ask_optional_date("Finish date (YYYY-MM-DD) boş bırak = bugün: ")
            rating = ask("Rating (1-5) boş bırak = yok: ")
            rating_val = int(rating) if rating.strip().isdigit() else None
            try:
                e = service.finish_reading(entry_id, d, rating_val)
                print(f"Bitti: {e.id} | status={e.status} | end={e.end_date} | rating={e.rating}")
            except KeyError:
                print("Hatalı entry_id.")
            except ValueError as ve:
                print(f"Hata: {ve}")

        elif choice == "10":
            print_books(service)
            book_id = ask("Yorum yazacağın book_id: ")
            text = ask("Yorum: ")
            spoiler = ask("Spoiler mı? (y/n): ").lower() == "y"
            try:
                r = service.write_review(user_id=user.id, book_id=book_id, text=text, spoiler=spoiler)
                print(f"Yorum kaydedildi: {r.id}")
            except KeyError:
                print("Hatalı book_id veya user yok.")

        elif choice == "11":
            # RAM -> JSON kaydet
            storage.save(service.books, service.users, service.entries, service.reviews)
            print("Kaydedildi. Görüşürüz.")
            break

        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
from __future__ import annotations  # Tipleri (class'ları) dosya içinde daha rahat referanslamak için

from datetime import date, datetime
from typing import Dict, List, Optional 
from uuid import uuid4  # !! Her objeye benzersiz id üretmek için (string'e çeviriyoruz)

from models.book import Book
from models.user import User
from models.reading_entry import ReadingEntry, ReadingStatus
from models.review import Review


class LibraryService:

    def __init__(self): # Dict kullanmamızın nedeni, id'ye göre hızlı erişim sağlamak. (O(1) erişim süresi)
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.entries: Dict[str, ReadingEntry] = {}
        self.reviews: Dict[str, Review] = {}

    # --------------------------- User işlemleri ---------------------------          
    def create_user(self, username: str, password_hash: str) -> User: # uuid4() rastgele benzersiz id üretir, str() ile string'e çeviriyoruz.
        user = User(
            id=str(uuid4()),
            username=username,
            password_hash=password_hash,  # Şimdilik "hash" diye isimlendirildi; ileride gerçekten hashlenecek
        )
        # Kullanıcıyı bellekte saklanır daha sonra JSON/DB'ye kaydedilir.
        self.users[user.id] = user
        return user

    def get_user(self, user_id: str) -> User:
        if user_id not in self.users:
            raise KeyError(f"User with id {user_id} not found.")
        return self.users[user_id]

    # --------------------------- Book işlemleri ---------------------------
    def add_book(self, title: str, author: str) -> Book: 
        book = Book(
            id=str(uuid4()), # Her kitap için benzersiz id oluşturulur
            title=title,
            author=author,
        )
        self.books[book.id] = book
        return book

    def get_book(self, book_id: str) -> Book: 
        if book_id not in self.books:
            raise KeyError(f"Book with id {book_id} not found.")
        return self.books[book_id]

    def list_books(self) -> List[Book]: # dict.values() -> Book objelerini verir; list(...) ile listeye çeviriyoruz.
        return list(self.books.values())

    # --------------------------- ReadingEntry işlemleri ---------------------------
    def add_to_library(self, user_id: str, book_id: str) -> ReadingEntry:
     # user ve book mevcut mu? (yoksa KeyError)
        _ = self.users[user_id]
        _ = self.books[book_id]

        entry = ReadingEntry(
            id=str(uuid4()),
            user_id=user_id,
            book_id=book_id,
            # status verilmezse ReadingEntry içinde default WANT olacak
        )
        self.entries[entry.id] = entry
        return entry

    def get_entry(self, entry_id: str) -> ReadingEntry:
        return self.entries[entry_id]

    def list_user_entries( self, user_id: str, status: Optional[ReadingStatus] = None) -> List[ReadingEntry]:
        items = [e for e in self.entries.values() if e.user_id == user_id]

        # status None değilse filtre uygula
        if status is not None:
            items = [e for e in items if e.status == status]

        return items

    def start_reading(self, entry_id: str, d: Optional[date] = None) -> ReadingEntry:
        entry = self.entries[entry_id]
        entry.start(d)  
        return entry

    def finish_reading(
        self,
        entry_id: str,
        d: Optional[date] = None,
        rating: Optional[int] = None,
    ) -> ReadingEntry:
        entry = self.entries[entry_id]
        entry.finish(d)

        if rating is not None:
            entry.set_rating(rating)

        return entry

    def abandon(self, entry_id: str) -> ReadingEntry:
        entry = self.entries[entry_id]
        entry.status = ReadingStatus.ABANDONED
        return entry

    # --------------------------- Review işlemleri ---------------------------
    def write_review(self, user_id: str, book_id: str, text: str, spoiler: bool = False) -> Review:
        # user ve book var mı kontrol (yoksa KeyError)
        _ = self.users[user_id]
        _ = self.books[book_id]

        review = Review(
            id=str(uuid4()),
            user_id=user_id,
            book_id=book_id,
            text=text,
            created_at=datetime.now(),  # Yorumun yazıldığı anki tarih ve saat
            spoiler=spoiler,
        )
        self.reviews[review.id] = review
        return review

    def list_book_reviews(self, book_id: str) -> List[Review]:
        # İstenen kitap_id'ye ait review'ları filtreliyoruz
        return [r for r in self.reviews.values() if r.book_id == book_id]
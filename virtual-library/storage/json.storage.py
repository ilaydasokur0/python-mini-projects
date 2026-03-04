import json
from pathlib import Path
from dataclasses import asdict
from typing import Dict

from models.book import Book
from models.user import User
from models.reading_entry import ReadingEntry
from models.review import Review


class JsonStorage:
    def __init__(self, file_path: str = "data/library_data.json"):
        self.file_path = Path(file_path)

    def save(
        self,
        books: Dict[str, Book],
        users: Dict[str, User],
        entries: Dict[str, ReadingEntry],
        reviews: Dict[str, Review],
    ):
        data = {
            "books": [asdict(book) for book in books.values()], # asdict() -> dataclass objelerini dict'e çevirir, böylece JSON'a yazılabilir hale gelir.
            "users": [asdict(user) for user in users.values()],
            "entries": [asdict(entry) for entry in entries.values()],
            "reviews": [asdict(review) for review in reviews.values()],
        }

        with open(self.file_path, "w", encoding="utf-8") as f: # JSON dosyasına verileri yazarken UTF-8 encoding kullanılır, böylece Türkçe karakterler gibi özel karakterler doğru şekilde saklanır.
            json.dump(data, f, indent=2)

    def load(self):

        if not self.file_path.exists():
            return {}, {}, {}, {} # Dosya yoksa boş dict'ler döndürür, böylece uygulama sıfırdan başlayabilir.

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        books = {b["id"]: Book(**b) for b in data.get("books", [])} #**b -> JSON'dan gelen dict'ler Book objelerine dönüştürülür.
        users = {u["id"]: User(**u) for u in data.get("users", [])}
        entries = {e["id"]: ReadingEntry(**e) for e in data.get("entries", [])}
        reviews = {r["id"]: Review(**r) for r in data.get("reviews", [])}

        return books, users, entries, reviews
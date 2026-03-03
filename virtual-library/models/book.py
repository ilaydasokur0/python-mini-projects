from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Book:
    id: str                 # uuid gibi düşünebilirsin, string tutacağız
    title: str
    author: str
    isbn: Optional[str] = None
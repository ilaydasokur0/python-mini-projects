from dataclasses import dataclass
from datetime import datetime

@dataclass
class Review:
    id: str
    user_id: str
    book_id: str
    text: str
    created_at: datetime
    spoiler: bool = False # Indicates whether the review contains spoilers, default is False
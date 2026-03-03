from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional

class ReadingStatus(str, Enum):
    WANT = "want"
    READING = "reading"
    FINISHED = "finished"
    ABANDONED = "abandoned"

@dataclass
class ReadingEntry:
    id: str
    user_id: str
    book_id: str
    status: ReadingStatus = ReadingStatus.WANT
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    rating: Optional[int] = None  # 1-5
    private_note: str = ""

    def start(self, d: Optional[date] = None):
        self.status = ReadingStatus.READING
        if self.start_date is None:
            self.start_date = d or date.today()

    def finish(self, d: Optional[date] = None):
        self.status = ReadingStatus.FINISHED
        if self.start_date is None:
            self.start_date = date.today()
        self.end_date = d or date.today()
        self._validate_dates()

    def set_rating(self, rating: int):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.rating = rating

    def _validate_dates(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValueError("end_date cannot be earlier than start_date.")
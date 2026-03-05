from dataclasses import dataclass
from datetime import date
from enum import Enum 
from typing import Optional

class ReadingStatus(str, Enum): # Enum class oluşturularak, okuma durumları için sabit değerler tanımlanır, bu da kodun daha okunabilir ve hatasız olmasını sağlar.
    WANT = "want"
    READING = "reading"
    FINISHED = "finished"
    ABANDONED = "abandoned"

@dataclass
class ReadingEntry: # ReadingEntry dataclass olarak oluşturulur, bu sınıf bir kullanıcının bir kitabı okuma durumunu ve ilgili bilgileri tutar.
    id: str
    user_id: str
    book_id: str
    status: ReadingStatus = ReadingStatus.WANT 
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    rating: Optional[int] = None  
    private_note: str = "" 

    def start(self, d: Optional[date] = None):
        self.status = ReadingStatus.READING # Okuma durumunu "reading" olarak günceller.
        if self.start_date is None:
            self.start_date = d or date.today() # Eğer start_date zaten belirlenmemişse, verilen tarih veya bugünün tarihi ile başlatır.

    def finish(self, d: Optional[date] = None): 
        self.status = ReadingStatus.FINISHED # Okuma durumunu "finished" olarak günceller.
        if self.start_date is None:
            self.start_date = date.today() # Eğer start_date belirlenmemişse, bugünün tarihi ile başlatır.
        self.end_date = d or date.today() # end_date'yi verilen tarih veya bugünün tarihi olarak ayarlar.
        self._validate_dates() # Tarihlerin geçerli olup olmadığını kontrol eder, end_date'nin start_date'den önce olmamasını sağlar.

    def set_rating(self, rating: int):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.rating = rating

    def _validate_dates(self): # start_date ve end_date'nin geçerli olup olmadığını kontrol eder, end_date'nin start_date'den önce olmamasını sağlar.
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValueError("end_date cannot be earlier than start_date.")
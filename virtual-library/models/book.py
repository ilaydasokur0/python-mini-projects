from dataclasses import dataclass # dataclass, veri sınıflarını tanımlamak için kullanılır, __init__, __repr__, __eq__ gibi özel yöntemler otomatik olarak oluşturulur.
from typing import Optional # değişkenin None olabileceğini belirtmek için kullanılır, bu da daha güvenli ve okunabilir kod yazmaya yardımcı olur.

@dataclass(frozen=True) # frozen=True ile oluşturulan dataclass'ler immutable olur, oluşturulduktan sonra özellikleri değiştirilemez, bu da veri bütünlüğünü sağlar.
class Book: 
    id: str                 
    title: str
    author: str
from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    id: str
    username: str
    password_hash: str 
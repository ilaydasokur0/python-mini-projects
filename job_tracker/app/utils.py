import re
from typing import Iterable, List

def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s\+\#\.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_skills(requirements_text: str, keywords: Iterable[str]) -> List[str]:
    if not requirements_text:
        return []

    text = normalize_text(requirements_text)
    found: List[str] = []

    for kw in keywords:
        kw_norm = normalize_text(kw)
        pattern = r"\b" + re.escape(kw_norm) + r"\b"
        if re.search(pattern, text):
            found.append(kw)

    return sorted(set(found), key=lambda x: x.lower())
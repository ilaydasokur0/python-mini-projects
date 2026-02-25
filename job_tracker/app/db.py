import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]  # job_tracker/
DB_PATH = BASE_DIR / "data" / "job_tracker.db"


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")  # ON DELETE CASCADE için
    return conn


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            requirements_text TEXT,
            link TEXT,
            notes TEXT
        )
        """)

        conn.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_id INTEGER NOT NULL,
            skill TEXT NOT NULL,
            source TEXT NOT NULL DEFAULT 'parsed',
            UNIQUE(app_id, skill),
            FOREIGN KEY(app_id) REFERENCES applications(id) ON DELETE CASCADE
        )
        """)

        conn.commit()
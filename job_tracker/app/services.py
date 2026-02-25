from datetime import date
from typing import Optional

from .db import get_conn
from .constants import STATUSES, SKILL_KEYWORDS
from .utils import extract_skills


def add_application(
    company: str,
    role: str,
    status: str = "Applied",
    requirements_text: str = "",
    link: str = "",
    notes: str = "",
) -> int:
    company = company.strip()
    role = role.strip()
    status = (status or "Applied").strip()

    if not company or not role:
        raise ValueError("Company and role are required.")
    if status not in STATUSES:
        raise ValueError(f"Invalid status: {status}. Options: {', '.join(STATUSES)}")

    today = date.today().isoformat()

    with get_conn() as conn:
        cur = conn.execute(
            """INSERT INTO applications
               (company, role, status, created_at, updated_at, requirements_text, link, notes)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (company, role, status, today, today, requirements_text.strip(), link.strip(), notes.strip()),
        )

        app_id = cur.lastrowid
        if app_id is None:
            raise RuntimeError("Insert failed: lastrowid is None")

        skills = extract_skills(requirements_text, SKILL_KEYWORDS)
        for s in skills:
            conn.execute(
                "INSERT OR IGNORE INTO skills (app_id, skill, source) VALUES (?, ?, 'parsed')",
                (app_id, s),
            )

        conn.commit()
        return app_id


def list_applications(status: Optional[str] = None):
    with get_conn() as conn:
        if status:
            rows = conn.execute(
                """SELECT id, company, role, status, created_at, updated_at
                   FROM applications
                   WHERE status = ?
                   ORDER BY created_at DESC""",
                (status,),
            ).fetchall()
        else:
            rows = conn.execute(
                """SELECT id, company, role, status, created_at, updated_at
                   FROM applications
                   ORDER BY created_at DESC"""
            ).fetchall()
    return rows


def top_skills(limit: int = 10):
    with get_conn() as conn:
        rows = conn.execute(
            """SELECT skill, COUNT(*) AS freq
               FROM skills
               GROUP BY skill
               ORDER BY freq DESC, skill ASC
               LIMIT ?""",
            (limit,),
        ).fetchall()
    return rows
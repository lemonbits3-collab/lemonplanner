# notizen_db.py
# Mini-SQLite-Layer für Notizen (MVP)
# Legt automatisch eine DB unter data/notizen.db an.

import sqlite3, os

DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "notizen.db")
_conn = None  # Singleton-Verbindung

def _ensure_db():
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            folder TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn

def get_conn():
    global _conn
    if _conn is None:
        _conn = _ensure_db()
    return _conn

def add_note(title: str, content: str, tags: str = "", folder: str = ""):
    c = get_conn()
    c.execute(
        "INSERT INTO notes (title, content, tags, folder) VALUES (?, ?, ?, ?)",
        (title, content, tags, folder)
    )
    c.commit()

def list_notes(search: str = ""):
    c = get_conn()
    sql = "SELECT id, title, content, tags, folder, created_at FROM notes"
    args = []
    if search:
        sql += " WHERE title LIKE ? OR content LIKE ? OR tags LIKE ?"
        like = f"%{search}%"
        args = [like, like, like]
    sql += " ORDER BY datetime(created_at) DESC"
    return c.execute(sql, args).fetchall()

def delete_note(note_id: int):
    c = get_conn()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    c.commit()

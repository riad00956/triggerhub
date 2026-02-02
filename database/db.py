import sqlite3
from pathlib import Path

DB_PATH = Path("uptime.db")

def get_connection():
    """
    Returns a SQLite connection object
    """
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # dict-like rows
    return conn

# Singleton connection (optional)
db_conn = get_connection()

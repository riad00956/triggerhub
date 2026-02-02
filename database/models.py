from database.db import db_conn

def init_db():
    cursor = db_conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            plan TEXT DEFAULT 'BASIC',   -- BASIC / PRIME
            premium_expire INTEGER DEFAULT NULL,
            joined_at INTEGER
        )
    """)

    # Monitors table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS monitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            url TEXT,
            interval INTEGER,
            status TEXT DEFAULT 'active', -- active / paused / expired
            created_at INTEGER,
            expire_at INTEGER DEFAULT NULL
        )
    """)

    # Logs table (PRIME can view)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            monitor_id INTEGER,
            status TEXT,
            reason TEXT,
            response_time INTEGER,
            created_at INTEGER
        )
    """)

    # Admin logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_id INTEGER,
            action TEXT,
            target_user INTEGER,
            created_at INTEGER
        )
    """)

    db_conn.commit()

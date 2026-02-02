from database.db import db_conn
import time

# ---------------------------
# Users
# ---------------------------
def get_user(user_id):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    return cursor.fetchone()

def create_user(user_id, username):
    cursor = db_conn.cursor()
    now = int(time.time())
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, username, joined_at) VALUES (?, ?, ?)",
        (user_id, username, now)
    )
    db_conn.commit()

def update_user_plan(user_id, plan, expire=None):
    cursor = db_conn.cursor()
    cursor.execute(
        "UPDATE users SET plan=?, premium_expire=? WHERE user_id=?",
        (plan, expire, user_id)
    )
    db_conn.commit()


# ---------------------------
# Monitors
# ---------------------------
def add_monitor(user_id, url, interval, expire=None):
    cursor = db_conn.cursor()
    now = int(time.time())
    cursor.execute(
        "INSERT INTO monitors (user_id, url, interval, created_at, expire_at) VALUES (?, ?, ?, ?, ?)",
        (user_id, url, interval, now, expire)
    )
    db_conn.commit()
    return cursor.lastrowid

def get_active_monitors():
    cursor = db_conn.cursor()
    now = int(time.time())
    cursor.execute(
        "SELECT * FROM monitors WHERE status='active' AND (expire_at IS NULL OR expire_at>?)",
        (now,)
    )
    return cursor.fetchall()

def get_user_monitors(user_id):
    cursor = db_conn.cursor()
    now = int(time.time())
    cursor.execute(
        "SELECT * FROM monitors WHERE user_id=? AND (expire_at IS NULL OR expire_at>?)",
        (user_id, now)
    )
    return cursor.fetchall()

def update_monitor_status(monitor_id, status):
    cursor = db_conn.cursor()
    cursor.execute("UPDATE monitors SET status=? WHERE id=?", (status, monitor_id))
    db_conn.commit()

def delete_monitor(monitor_id):
    cursor = db_conn.cursor()
    cursor.execute("DELETE FROM monitors WHERE id=?", (monitor_id,))
    db_conn.commit()

# ---------------------------
# Logs
# ---------------------------
def add_log(monitor_id, status, reason, response_time):
    cursor = db_conn.cursor()
    now = int(time.time())
    cursor.execute(
        "INSERT INTO logs (monitor_id, status, reason, response_time, created_at) VALUES (?, ?, ?, ?, ?)",
        (monitor_id, status, reason, response_time, now)
    )
    db_conn.commit()

def get_logs(monitor_id, limit=20):
    cursor = db_conn.cursor()
    cursor.execute(
        "SELECT * FROM logs WHERE monitor_id=? ORDER BY created_at DESC LIMIT ?",
        (monitor_id, limit)
    )
    return cursor.fetchall()

# ---------------------------
# Admin Logs
# ---------------------------
def add_admin_log(admin_id, action, target_user):
    cursor = db_conn.cursor()
    now = int(time.time())
    cursor.execute(
        "INSERT INTO admin_logs (admin_id, action, target_user, created_at) VALUES (?, ?, ?, ?)",
        (admin_id, action, target_user, now)
    )
    db_conn.commit()

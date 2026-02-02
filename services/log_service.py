from database.queries import add_log, get_logs
from services.prime_service import is_prime

def save_log(monitor_id, status, reason, response_time):
    add_log(monitor_id, status, reason, response_time)

def fetch_logs(user_id, monitor_id, limit=20):
    # Only PRIME users can view logs
    if not is_prime(user_id):
        return []
    return get_logs(monitor_id, limit)

def debug_status(user_id, monitor_id):
    """
    Return last ping status for PRIME users
    """
    logs = fetch_logs(user_id, monitor_id, limit=1)
    if logs:
        l = logs[0]
        return f"🌐 Last: {l['status']}, {l['reason']}, {l['response_time']}ms"
    return "No data yet"

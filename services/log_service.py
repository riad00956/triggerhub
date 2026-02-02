from database.queries import add_log, get_logs
from services.prime_service import is_prime

def save_log(monitor_id, status, reason, response_time):
    add_log(monitor_id, status, reason, response_time)

def fetch_logs(user_id, monitor_id, limit=20):
    # Only PRIME users can view logs
    if not is_prime(user_id):
        return []
    return get_logs(monitor_id, limit)

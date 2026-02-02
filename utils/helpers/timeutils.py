from utils.timeutils import now_ts, calculate_expiry, remaining_time, format_seconds

# Wrapper functions for helpers
def current_timestamp():
    return now_ts()

def expiry_after(seconds: int):
    return calculate_expiry(seconds)

def time_left(expire_ts: int):
    return remaining_time(expire_ts)

def human_readable(sec: int):
    return format_seconds(sec)

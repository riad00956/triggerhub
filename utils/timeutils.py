import time

def now_ts() -> int:
    return int(time.time())

def calculate_expiry(seconds: int) -> int:
    """
    Returns timestamp of expiry from now
    """
    return int(time.time()) + seconds

def remaining_time(expire_ts: int) -> int:
    """
    Returns remaining seconds until expiry
    """
    remaining = expire_ts - int(time.time())
    return max(0, remaining)

def format_seconds(sec: int) -> str:
    """
    Returns human readable string like 01:23:45
    """
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

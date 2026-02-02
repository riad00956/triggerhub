import time
from database.queries import get_user, create_user, get_user_monitors

def ensure_user(user_id, username=None):
    """
    Create user if not exists
    """
    user = get_user(user_id)
    if not user:
        create_user(user_id, username)
        user = get_user(user_id)
    return user

def can_add_monitor(user_id):
    user = get_user(user_id)
    monitors = get_user_monitors(user_id)
    plan = user["plan"]
    from core.limits import can_add_monitor
    return can_add_monitor(plan, len(monitors))

def get_user_plan(user_id):
    user = get_user(user_id)
    return user["plan"] if user else "BASIC"

def get_remaining_time(user_id):
    """
    Returns seconds remaining for Basic monitor expiry
    """
    monitors = get_user_monitors(user_id)
    now = int(time.time())
    remaining = 0
    for m in monitors:
        if m["expire_at"]:
            rem = m["expire_at"] - now
            if rem > remaining:
                remaining = rem
    return remaining

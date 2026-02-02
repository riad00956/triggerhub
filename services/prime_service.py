import time
from database.queries import update_user_plan, get_user
from core.restore import restore_jobs

def add_prime(user_id, days=7):
    """
    Activate PRIME for given user_id
    """
    now = int(time.time())
    expire = now + days*24*3600
    update_user_plan(user_id, "PRIME", expire)
    # After activation, restore jobs (unlimited interval etc)
    restore_jobs()
    return expire

def remove_prime(user_id):
    update_user_plan(user_id, "BASIC", None)

def is_prime(user_id):
    user = get_user(user_id)
    if not user:
        return False
    plan = user["plan"]
    expire = user["premium_expire"]
    now = int(time.time())
    if plan == "PRIME" and (expire is None or expire > now):
        return True
    elif plan == "PRIME" and expire <= now:
        # Auto downgrade
        remove_prime(user_id)
        return False
    return False

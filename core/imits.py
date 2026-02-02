from config import (
    BASIC_MAX_MONITORS,
    BASIC_MAX_TIME,
    PRIME_MAX_MONITORS
)

def can_add_monitor(user_plan, current_count):
    if user_plan == "PRIME":
        return True

    return current_count < BASIC_MAX_MONITORS


def get_allowed_interval(user_plan):
    if user_plan == "PRIME":
        return None  # unlimited / custom

    return [5, 10]  # fixed for BASIC


def get_expiry_seconds(user_plan):
    if user_plan == "PRIME":
        return None

    return BASIC_MAX_TIME  # 1 hour


def can_view_debug(user_plan):
    return user_plan == "PRIME"

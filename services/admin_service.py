from database.queries import add_admin_log
from services.prime_service import add_prime, remove_prime

def grant_prime(admin_id, target_user_id, days=7):
    expire = add_prime(target_user_id, days)
    add_admin_log(admin_id, f"Grant PRIME {days} days", target_user_id)
    return expire

def revoke_prime(admin_id, target_user_id):
    remove_prime(target_user_id)
    add_admin_log(admin_id, "Revoke PRIME", target_user_id)

def log_admin_action(admin_id, action, target_user_id):
    add_admin_log(admin_id, action, target_user_id)

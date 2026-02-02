from bot.instance import bot
from bot.keyboards import home_keyboard
from bot.messages import HOME_TEXT
from services.admin_service import grant_prime, revoke_prime, log_admin_action
from services.user_service import get_user_plan, ensure_user
from utils.cleaner import edit_or_send

ADMIN_IDS = [12345678]  # Replace with your admin Telegram ID(s)

@bot.callback_query_handler(func=lambda call: call.from_user.id in ADMIN_IDS)
def admin_router(call):
    data = call.data
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    if data.startswith("grantprime_"):
        _, user_id, days = data.split("_")
        expire = grant_prime(call.from_user.id, int(user_id), int(days))
        edit_or_send(chat_id, f"✅ Granted PRIME to {user_id} for {days} days", msg_id)

    elif data.startswith("revokeprime_"):
        _, user_id = data.split("_")
        revoke_prime(call.from_user.id, int(user_id))
        edit_or_send(chat_id, f"❌ Revoked PRIME from {user_id}", msg_id)

    elif data.startswith("viewlogs_"):
        # Example: view last 10 logs
        from services.log_service import fetch_logs
        _, monitor_id = data.split("_")
        logs = fetch_logs(call.from_user.id, int(monitor_id))
        text = "📜 Logs:\n"
        for l in logs:
            text += f"{l['status']} - {l['reason']} ({l['response_time']}ms)\n"
        edit_or_send(chat_id, text or "No logs", msg_id)

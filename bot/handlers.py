from bot.instance import bot
from bot.keyboards import home_keyboard, interval_keyboard, monitor_options_keyboard
from bot.messages import *
from utils.validators import is_valid_url
from utils.cleaner import edit_or_send, delete_user_message
from database.queries import add_monitor, get_user_monitors
from services.user_service import ensure_user, can_add_monitor, get_user_plan
from services.prime_service import is_prime
from core.scheduler import add_job
from core.monitor import ping_url
from utils.timeutils import calculate_expiry, human_readable

# -----------------------------
# /start handler
# -----------------------------
@bot.message_handler(commands=['start'])
def start(message):
    ensure_user(message.from_user.id, message.from_user.username)
    plan = get_user_plan(message.from_user.id)
    edit_or_send(
        chat_id=message.chat.id,
        text=HOME_TEXT.format(plan=plan),
        reply_markup=home_keyboard()
    )

# -----------------------------
# URL input handler
# -----------------------------
@bot.message_handler(func=lambda m: True)
def handle_url(message):
    if not is_valid_url(message.text):
        edit_or_send(message.chat.id, "❌ Invalid URL")
        delete_user_message(message.chat.id, message.message_id)
        return

    # Save basic monitor (interval 0 for now)
    row_id = add_monitor(message.from_user.id, message.text, 0, expire=calculate_expiry(3600))  # 1 hour for BASIC
    delete_user_message(message.chat.id, message.message_id)
    edit_or_send(
        message.chat.id,
        "URL saved! Select interval:",
        reply_markup=interval_keyboard(row_id)
    )

# -----------------------------
# Callback query handler
# -----------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_router(call):
    data = call.data
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    if data == "home":
        plan = get_user_plan(call.from_user.id)
        edit_or_send(chat_id, HOME_TEXT.format(plan=plan), msg_id, home_keyboard())

    elif data.startswith("save_"):
        _, minutes, row_id = data.split("_")
        # Schedule the job
        url = [m['url'] for m in get_user_monitors(call.from_user.id) if str(m['id'])==row_id][0]
        add_job(f"job_{row_id}", ping_url, int(minutes), [int(row_id), call.from_user.id, url])
        edit_or_send(chat_id, SUCCESS_MONITOR_TEXT.format(url=url, expiry=minutes+" min"), msg_id, home_keyboard())

    elif data == "list":
        monitors = get_user_monitors(call.from_user.id)
        text = MY_MONITORS_TEXT
        for m in monitors:
            text += f"🌐 {m['url']} ({m['interval']} min)\n"
        edit_or_send(chat_id, text or "No monitors yet.", msg_id)

    elif data == "prime":
        text = PRIME_TEXT.format(status="Active" if is_prime(call.from_user.id) else "Not Active")
        edit_or_send(chat_id, text, msg_id)

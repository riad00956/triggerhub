from telebot import types

def home_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("➕ Add Monitor", callback_data="add"),
        types.InlineKeyboardButton("📋 My Monitors", callback_data="list")
    )
    markup.add(
        types.InlineKeyboardButton("💎 PRIME Subscription", callback_data="prime"),
        types.InlineKeyboardButton("⚙ Settings", callback_data="settings")
    )
    return markup

def interval_keyboard(row_id):
    markup = types.InlineKeyboardMarkup()
    buttons = [types.InlineKeyboardButton(f"{m} min", callback_data=f"save_{m}_{row_id}") for m in [5,10,30]]
    markup.add(*buttons)
    markup.add(types.InlineKeyboardButton("⬅️ Back", callback_data="home"))
    return markup

def monitor_options_keyboard(monitor_id, is_prime=False):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("⏸ Pause", callback_data=f"pause_{monitor_id}"),
        types.InlineKeyboardButton("🔄 Ping Now", callback_data=f"ping_{monitor_id}")
    )
    if is_prime:
        markup.add(types.InlineKeyboardButton("🧪 Live Debug", callback_data=f"debug_{monitor_id}"))
    markup.add(types.InlineKeyboardButton("🗑 Delete", callback_data=f"delete_{monitor_id}"))
    markup.add(types.InlineKeyboardButton("⬅️ Back", callback_data="list"))
    return markup

def pagination_keyboard(prev_callback=None, next_callback=None):
    markup = types.InlineKeyboardMarkup()
    buttons = []
    if prev_callback:
        buttons.append(types.InlineKeyboardButton("⬅️ Prev", callback_data=prev_callback))
    if next_callback:
        buttons.append(types.InlineKeyboardButton("➡️ Next", callback_data=next_callback))
    if buttons:
        markup.add(*buttons)
    markup.add(types.InlineKeyboardButton("🏠 Home", callback_data="home"))
    return markup

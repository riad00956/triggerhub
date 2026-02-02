from bot.instance import bot
from telebot.types import InlineKeyboardMarkup

def edit_or_send(chat_id, text, message_id=None, reply_markup: InlineKeyboardMarkup = None):
    """
    Edits existing message if message_id provided,
    else sends new message.
    Ensures ONE MESSAGE POLICY
    """
    try:
        if message_id:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                  text=text, reply_markup=reply_markup)
        else:
            bot.send_message(chat_id, text, reply_markup=reply_markup)
    except:
        # fallback: send new message
        bot.send_message(chat_id, text, reply_markup=reply_markup)

def delete_user_message(chat_id, message_id):
    """
    Deletes a user input message to keep chat clean
    """
    try:
        bot.delete_message(chat_id, message_id)
    except:
        pass

from bot.instance import bot
from core.scheduler import start_scheduler
from core.restore import restore_jobs

restore_jobs()
start_scheduler()
bot.infinity_polling()

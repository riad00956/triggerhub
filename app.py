from bot.instance import bot
from core.scheduler import start_scheduler
from core.restore import restore_jobs

if __name__ == "__main__":
    # Restore jobs from DB
    restore_jobs()
    
    # Start APScheduler
    start_scheduler()
    
    # Start bot polling (infinite)
    bot.infinity_polling()

from apscheduler.schedulers.background import BackgroundScheduler
from config import TIMEZONE

scheduler = BackgroundScheduler(timezone=TIMEZONE)

def start_scheduler():
    if not scheduler.running:
        scheduler.start()

def add_job(job_id, func, minutes, args):
    if scheduler.get_job(job_id):
        return
    scheduler.add_job(
        func,
        trigger="interval",
        minutes=minutes,
        args=args,
        id=job_id,
        replace_existing=True,
        max_instances=1
    )

def remove_job(job_id):
    try:
        scheduler.remove_job(job_id)
    except:
        pass

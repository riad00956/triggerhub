from database.queries import get_active_monitors
from core.scheduler import add_job
from core.monitor import ping_url

def restore_jobs():
    """
    Bot restart হলে DB থেকে সব active monitor
    আবার scheduler-এ add করবে
    """
    monitors = get_active_monitors()

    for m in monitors:
        job_id = f"monitor_{m['id']}"

        add_job(
            job_id=job_id,
            func=ping_url,
            minutes=m["interval"],
            args=[m["id"], m["user_id"], m["url"]]
        )

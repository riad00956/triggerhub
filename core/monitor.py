import time
import requests
from services.log_service import save_log, debug_status
from services.user_service import get_user_plan
from services.user_service import get_user_plan
from services.user_service import get_user_plan
from services.user_service import get_user_plan

def ping_url(monitor_id, user_id, url):
    start = time.time()
    status = "UP"
    reason = "OK"
    response_time = None

    try:
        r = requests.get(url, timeout=10, allow_redirects=True)
        response_time = int((time.time() - start) * 1000)

        if r.status_code >= 400:
            status = "DOWN"
            reason = f"HTTP {r.status_code}"

    except requests.exceptions.Timeout:
        status = "DOWN"
        reason = "Timeout"

    except requests.exceptions.RequestException:
        status = "DOWN"
        reason = "Connection Error"

    # Save log
    save_log(
        monitor_id=monitor_id,
        status=status,
        reason=reason,
        response_time=response_time
    )

    # Notify user only if down
    if status == "DOWN":
        from bot.instance import bot
        bot.send_message(
            user_id,
            f"🚨 <b>DOWN</b>\n{url}\nReason: {reason}"
        )

    # PRIME debug message
    if get_user_plan(user_id) == "PRIME":
        last_status = debug_status(user_id, monitor_id)
        bot.send_message(
            user_id,
            f"🧪 Debug: {last_status}"
        )

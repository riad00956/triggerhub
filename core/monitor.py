import time
import requests
from services.log_service import save_log
from services.user_service import notify_user

TIMEOUT = 10

def ping_url(monitor_id, user_id, url):
    start = time.time()
    status = "UP"
    reason = "OK"
    response_time = None

    try:
        r = requests.get(url, timeout=TIMEOUT, allow_redirects=True)
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

    # Save log (PRIME users can view)
    save_log(
        monitor_id=monitor_id,
        status=status,
        reason=reason,
        response_time=response_time
    )

    # Notify only on DOWN
    if status == "DOWN":
        notify_user(
            user_id,
            f"🚨 <b>DOWN</b>\n{url}\nReason: {reason}"
        )

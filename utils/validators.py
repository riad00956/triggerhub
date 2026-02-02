import re
from urllib.parse import urlparse

BLOCKED_SCHEMES = ["file", "ftp", "smb"]
BLOCKED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

def is_valid_url(url: str) -> bool:
    """
    Validate URL:
    - Must start with http or https
    - Must be proper domain
    - Must not be localhost / internal IP
    """
    if not url.lower().startswith(("http://", "https://")):
        return False

    try:
        parsed = urlparse(url)
        if parsed.scheme not in ["http", "https"]:
            return False
        host = parsed.hostname
        if host in BLOCKED_HOSTS:
            return False
        return True
    except Exception:
        return False

def sanitize_text(text: str) -> str:
    """
    Clean text for sending in bot messages
    """
    return re.sub(r"[<>]", "", text)

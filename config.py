# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv


def _get_int(name, default=None):
    raw_value = getenv(name)
    if raw_value is None or raw_value == "":
        return default
    try:
        return int(raw_value)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"Invalid integer value for {name}: {raw_value!r}") from exc


def _get_int_list(name):
    raw_value = getenv(name, "")
    if not raw_value.strip():
        return []

    values = []
    for part in raw_value.split():
        try:
            values.append(int(part))
        except (TypeError, ValueError) as exc:
            raise RuntimeError(f"Invalid integer value for {name}: {part!r}") from exc
    return values


REQUIRED_ENV_VARS = ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_DB", "OWNER_ID", "CHANNEL_ID", "LOG_GROUP"]


for key in REQUIRED_ENV_VARS:
    value = getenv(key, "")
    if key in {"OWNER_ID", "CHANNEL_ID", "API_ID"}:
        if key == "OWNER_ID":
            if not value.strip():
                raise RuntimeError(
                    f"Missing required environment variable: {key}. Set OWNER_ID to one or more numeric Telegram user IDs."
                )
        elif value in (None, ""):
            raise RuntimeError(
                f"Missing required environment variable: {key}. Set {key} before starting the bot."
            )
    elif value in (None, ""):
        raise RuntimeError(
            f"Missing required environment variable: {key}. Set {key} before starting the bot."
        )


# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = _get_int("API_ID")
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = _get_int_list("OWNER_ID")
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = _get_int("CHANNEL_ID")
FREEMIUM_LIMIT = _get_int("FREEMIUM_LIMIT", 0)
PREMIUM_LIMIT = _get_int("PREMIUM_LIMIT", 500)
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAULT_SESSION") or getenv("DEFAUL_SESSION", None)  # keep legacy fallback
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)

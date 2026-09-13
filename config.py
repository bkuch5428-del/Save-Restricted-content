# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv


def _require_env(name, cast=None):
    value = getenv(name)
    if value is None or value == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    if cast is None:
        return value
    try:
        return cast(value)
    except Exception as exc:
        raise RuntimeError(f"Invalid environment variable value for {name}: {value!r}") from exc


API_ID = _require_env("API_ID", int)
API_HASH = _require_env("API_HASH")
BOT_TOKEN = _require_env("BOT_TOKEN")
OWNER_ID = _require_env("OWNER_ID", int)
MONGODB_CONNECTION_STRING = _require_env("MONGO_DB")
LOG_GROUP = _require_env("LOG_GROUP", int)
FORCESUB = _require_env("FORCESUB")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "")

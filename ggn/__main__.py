# Github / devgagnin

import logging
import os
import threading
import time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

botStartTime = time.time()

if __name__ == "__main__":
    import glob
    from pathlib import Path

    from app import app
    from ggn.importer import load_plugins

    port = int(os.environ.get("PORT", 10000))

    def start_health_server():
        app.run(host="0.0.0.0", port=port, use_reloader=False, threaded=True)

    threading.Thread(target=start_health_server, daemon=True).start()

    from . import bot

    path = "ggn/assets/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    logger.info("Bot Started :)")
    print("""
()   ()
(*_*)
(/ \\)""")

    bot.run_until_disconnected()
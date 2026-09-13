import os
import importlib.util
import pkgutil

if not hasattr(pkgutil, 'get_loader'):
    def _compat_get_loader(module_name):
        if module_name == '__main__':
            return None
        try:
            spec = importlib.util.find_spec(module_name)
        except (ImportError, ValueError):
            return None
        return spec.loader if spec is not None else None

    pkgutil.get_loader = _compat_get_loader

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <center>
        <img src="/static/livebot.png" style="border-radius: 2px;"/>
    </center>
    <style>
        body {
            background: antiquewhite;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100vh;
            margin: 0;
        }
        footer {
            text-align: center;
            padding: 10px;
            background: antiquewhite;
            font-size: 1.2em;
        }
    </style>
    <footer>
        Made with 💕 by Team SPY
    </footer>
    """


@app.route('/healthz')
def healthz():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

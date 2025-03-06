from flask import Flask, render_template
from gunicorn.app.base import BaseApplication

app = Flask(__name__, static_folder='static')

@app.route("/")
def home_route():
    return render_template("lun4rsocial.html")

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == "__main__":
    options = {
        "bind": "0.0.0.0:8080",
        "workers": 4,
        "loglevel": "info",
        "accesslog": "-",
        "preload_app": True
    }
    StandaloneApplication(app, options).run()

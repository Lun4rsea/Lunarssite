from flask import request
import logging
from flask import Flask, render_template, url_for
# from gunicorn.app.base import BaseApplication

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')

@app.before_request
def before_request():
    request.user_ip = request.headers.get('cf-connecting-ip')

@app.route("/")
def home_route():
    return render_template("Lun4rSocial.html", user_ip=request.user_ip)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

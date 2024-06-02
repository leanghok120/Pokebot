from flask import Flask
from threading import Thread

# Just a web server to keep this bot alive on replit
app = Flask("")


@app.route("/")
def home():
    return "Hello, I'm alive!"


def run():
    app.run(host="0.0.0.0", port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()

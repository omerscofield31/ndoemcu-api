from flask import Flask
import json
import requests

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"
@app.route("/api")
def nodemcu_get():
    doviz = requests.get('https://canlialtinfiyatlari.com/LIVE/total.php')

    return doviz.content

@app.route("/api1")
def nodemcu_get():
    doviz = requests.get('https://canlidovizkurlari.com/refresh/check.php')

    return doviz.content

if __name__ == "__main__":
    app.run()

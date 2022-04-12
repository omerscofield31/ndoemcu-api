from flask import Flask
import json
import requests

app = Flask(__name__)
@app.route("/")
def index():
    return "hello world"
@app.route("/api")
def nodemcu_get():
    doviz = requests.get('https://api.genelpara.com/embed/doviz.json')

    return doviz.content

if __name__ == "__main__":
    app.run()

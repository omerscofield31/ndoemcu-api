from flask import Flask
import json
import requests

app = Flask(__name__)


print(json.dumps(jsons))
@app.route("/api")
def nodemcu_get():
    doviz = requests.get('https://api.genelpara.com/embed/doviz.json')
    #altin = requests.get('https://api.genelpara.com/embed/altin.json')
    #py_altin = json.loads(altin)
    py_doviz = json.loads(doviz.content)

    jsons = {
    "1":{"1" : "Dolar/Tl",
    "2" : (py_doviz["USD"])["alis"],
    },
    "2":{"1" : "Gram/Tl",
    "2" : (py_doviz["USD"])["alis"],
    }
}
    return json.dumps(jsons)

if __name__ == "__main__":
    app.run()

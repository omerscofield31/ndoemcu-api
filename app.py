from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!!"
@app.route("/api/yb4fxvbx2q985j6aibzayofty")
def nodemcu_get():
    headers = {
'Host': 'servis.mgm.gov.tr',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Origin': 'https://www.mgm.gov.tr',
'Referer': 'https://www.mgm.gov.tr/',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site'
}
    doviz = requests.get('https://canlialtinfiyatlari.com/LIVE/total.php')
    hava = requests.get('https://servis.mgm.gov.tr/web/sondurumlar?merkezid=91009', headers=headers)
    havajs = json.loads(hava.content)
    py_doviz = json.loads(doviz.content)
    dolar = py_doviz["USDTRY"]
    ons = py_doviz["XAUUSD"]
    gr = dolar*ons/31.1
    ceyrek = gr*1.6065
    portfoy = dolar*120+gr*1.5+ceyrek
    derece = havajs[0]["sicaklik"]
    jsons = {
    "1": dolar,
    "2": round(gr),
    "3": round(ons),
    "4": round(portfoy),
    "5": derece
}
    return json.dumps(jsons)

if __name__ == "__main__":
    app.run()

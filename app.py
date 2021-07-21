from flask import *
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def jokes():
    url = "https://api.chucknorris.io/jokes/random"
    data = requests.get(url).json()
    return "<img src='{}'>" \
           "</img>" \
           "</br>" \
           "<strong>Joke:</strong> " \
           "{}".format(data['icon_url'], data)


@app.route("/category", methods=["GET"])
def smh():
    url = "https://api.chucknorris.io/jokes/categories"
    ata = requests.get(url).json()
    return "{}".format(ata)


if __name__ == '__main__':
    app.run(debug=True)

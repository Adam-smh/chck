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


if __name__ == '__main__':
    app.run(debug=True)
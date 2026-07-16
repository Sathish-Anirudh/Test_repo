import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/fetch")
def fetch():

    url = request.args.get("url")

    # SSRF Vulnerability
    response = requests.get(url)

    return response.text


@app.route("/download")
def download():

    target = request.args.get("target")

    # Another SSRF
    return requests.post(target).text


if __name__ == "__main__":
    app.run(debug=True)

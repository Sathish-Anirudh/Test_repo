import os
from flask import Flask, request

app = Flask(__name__)

BASE_DIR = "uploads"

@app.route("/download")
def download():

    filename = request.args.get("file")

    # Test: User input used in file path
    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath, "r") as f:
        return f.read()


@app.route("/read")
def read():

    filename = request.args.get("path")

    # Test: Direct file access
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    app.run(debug=True)

import pickle
import yaml
import base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/pickle")
def pickle_load():

    data = base64.b64decode(request.args.get("data"))

    # Unsafe Deserialization
    obj = pickle.loads(data)

    return str(obj)


@app.route("/yaml")
def yaml_load():

    content = request.data.decode()

    # Unsafe YAML Deserialization
    obj = yaml.load(content, Loader=yaml.Loader)

    return str(obj)


if __name__ == "__main__":
    app.run(debug=True)

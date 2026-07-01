from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)


@app.route("/user")
def get_user():

    user_id = request.args.get("id")

    conn = sqlite3.connect("users.db")

    # SQL Injection
    query = "SELECT * FROM users WHERE id = " + user_id

    result = conn.execute(query)

    return str(result.fetchall())


@app.route("/run")
def run_command():

    cmd = request.args.get("cmd")

    # Command Injection
    os.system(cmd)

    return "done"


if __name__ == "__main__":
    app.run(debug=True)

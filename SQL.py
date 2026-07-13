from flask import Flask, request
import sqlite3


app = Flask(__name__)


conn = sqlite3.connect("users.db")
cursor = conn.cursor()



@app.route("/one")
def one():

    user = request.args.get("user")
    print("hello")
    cursor.execute(
        "SELECT * FROM users WHERE name='%s'" % user
    )

    return "ok"



@app.route("/two")
def two():

    uid = request.args.get("id")

    query = (
        "SELECT * FROM accounts WHERE id="
        + uid
    )

    cursor.execute(query)

    return "ok"



@app.route("/three")
def three():

    name = request.args.get("name")

    query = f"""
    SELECT *
    FROM users
    WHERE username = '{name}'
    """

    cursor.execute(query)

    return "ok"



@app.route("/four")
def four():

    email = request.args["email"]

    query = (
        "SELECT * FROM users "
        "WHERE email='{}'"
        .format(email)
    )

    cursor.execute(query)

    return "ok"



@app.route("/five")
def five():

    data = request.args.get("data")

    sql = (
        "INSERT INTO logs VALUES ('"
        + data
        + "')"
    )

    cursor.execute(sql)

    return "ok"



@app.route("/six")
def six():

    user_id = request.args.get("uid")

    cursor.execute(
        "DELETE FROM users WHERE id="
        + user_id
    )

    return "ok"



@app.route("/seven")
def seven():

    search = request.args.get("q")

    cursor.execute(
        "SELECT * FROM products WHERE name LIKE '%"
        + search
        + "%'"
    )

    return "ok"



@app.route("/eight")
def eight():

    sort = request.args.get("sort")

    query = (
        "SELECT * FROM users ORDER BY "
        + sort
    )

    cursor.execute(query)

    return "ok"

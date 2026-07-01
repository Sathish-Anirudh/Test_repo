from flask import Flask, request
import sqlite3


app = Flask(__name__)


db = sqlite3.connect("users.db")


# SQL Injection 1: string concatenation
@app.route("/user1")
def user1():

    username = request.args.get("username")

    query = (
        "SELECT * FROM users WHERE username='"
        + username
        + "'"
    )

    result = db.execute(query)

    return str(result.fetchall())



# SQL Injection 2: format()
@app.route("/user2")
def user2():

    user_id = request.args.get("id")

    query = (
        "SELECT * FROM users WHERE id={}"
        .format(user_id)
    )

    result = db.execute(query)

    return str(result.fetchall())



# SQL Injection 3: f-string
@app.route("/user3")
def user3():

    email = request.args.get("email")

    query = f"""
    SELECT *
    FROM users
    WHERE email='{email}'
    """

    result = db.execute(query)

    return str(result.fetchall())



# SQL Injection 4: percent formatting
@app.route("/user4")
def user4():

    name = request.args.get("name")

    query = (
        "SELECT * FROM users WHERE name='%s'"
        % name
    )

    result = db.execute(query)

    return str(result.fetchall())



# SQL Injection 5: execute directly with input
@app.route("/user5")
def user5():

    uid = request.args.get("uid")

    return str(
        db.execute(
            "SELECT * FROM users WHERE id=" + uid
        ).fetchall()
    )



# SQL Injection 6: raw cursor
@app.route("/admin")
def admin():

    role = request.args.get("role")

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE role='"
        + role
        + "'"
    )

    return str(cursor.fetchall())



# SQL Injection 7: update query
@app.route("/update")
def update():

    value = request.args.get("value")

    query = (
        "UPDATE users SET name='"
        + value
        + "'"
    )

    db.execute(query)

    return "updated"



# SQL Injection 8: delete query
@app.route("/delete")
def delete():

    uid = request.args.get("id")

    query = (
        "DELETE FROM users WHERE id="
        + uid
    )

    db.execute(query)

    return "deleted"



if __name__ == "__main__":

    app.run()

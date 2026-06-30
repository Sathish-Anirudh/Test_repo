# test_access_control.py

from flask import Flask, request

app = Flask(__name__)


# -------------------------
# SAFE EXAMPLE
# -------------------------

@app.route("/profile")
def profile():

    user = get_current_user()

    if not user:
        return "Unauthorized"

    return user



# -------------------------
# VULNERABILITY 1
# Missing Authorization
# -------------------------

@app.route("/admin/delete")
def delete_user():

    user_id = request.args["id"]

    delete_account(user_id)

    return "deleted"



# -------------------------
# SAFE ADMIN CHECK
# -------------------------

@app.route("/admin/settings")
def settings():

    if current_user.role == "admin":

        return "settings"

    return "Forbidden"




# -------------------------
# VULNERABILITY 2
# Possible IDOR
# -------------------------

@app.route("/user")
def get_user():

    uid = request.args["id"]

    user = get_user_by_id(uid)

    return user




# -------------------------
# SAFE ID HANDLING
# -------------------------

@app.route("/my-account")
def my_account():

    user = get_current_user()

    return user




# -------------------------
# VULNERABILITY 3
# Hardcoded privilege
# -------------------------

ADMIN = True


def access_panel():

    if ADMIN:

        return "Admin panel"




# -------------------------
# VULNERABILITY 4
# Disabled auth
# -------------------------

AUTH_ENABLED = False



@app.route("/payment/delete")
def delete_payment():

    payment_id = request.json["id"]

    remove_payment(payment_id)




# -------------------------
# NORMAL CODE
# -------------------------

def calculate_total():

    price = 100

    tax = 10

    return price + tax



# fake functions

def delete_account(id):
    pass


def get_user_by_id(id):
    pass


def remove_payment(id):
    pass


def get_current_user():
    pass

from flask import Flask
import requests
import hashlib
import subprocess
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

@app.route("/")
def home():
    return "Hello"

# SQL Injection
@app.route("/user/<id>")
def get_user(id):
    query = "SELECT * FROM users WHERE id=" + id
    cursor.execute(query)
    return "Done"

# Command Injection
@app.route("/ping/<host>")
def ping(host):
    subprocess.call("ping " + host, shell=True)
    return "Done"

# Weak Crypto
@app.route("/hash/<text>")
def hash_text(text):
    return hashlib.md5(text.encode()).hexdigest()

# SSL Verification Disabled
@app.route("/request")
def insecure_request():
    requests.get("https://google.com", verify=False)
    return "Done"

app.run(host="0.0.0.0", port=5000, debug=True)
GITHUB_TOKEN = "ghp_123456789012345678901234567890123456"
password ="jnmfndjgktmrnejfdkcmkvfnrjekwddefgvef323456543wse32qASDiok"
DB_PASSWORD = "ASDFfhjnbvhngjfkdmcvf123456789012345678901234567890123456"
API_PASSWORD = "ASDFfhjnbvhngjfkdmcvf123456789012345678901234567890123456"

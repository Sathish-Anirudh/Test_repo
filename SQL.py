import sqlite3


connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM users"
)

user_id = 10

cursor.execute(
    "SELECT * FROM users WHERE id=?",
    (user_id,)
)


username = "john"

cursor.execute(
    "INSERT INTO users(name) VALUES(?)",
    (username,)
)


cursor.execute(
    "UPDATE users SET active=? WHERE id=?",
    (1, user_id)
)


name = input("Enter username: ")


query1 = (
    "SELECT * FROM users WHERE name='"
    + name
    + "'"
)


cursor.execute(query1)

email = input("Email: ")


query2 = f"""
SELECT *
FROM users
WHERE email='{email}'
"""


cursor.execute(query2)



uid = input("ID: ")


query3 = (
    "SELECT * FROM users WHERE id={}"
    .format(uid)
)


cursor.execute(query3)

search = input("Search: ")


dynamic_query = (
    "SELECT * FROM products WHERE name='"
    + search
    + "'"
)


cursor.execute(dynamic_query)





bad_query1 = """
SELECT *
FROM users
WHERE username='admin'
OR 1=1
"""


bad_query2 = """
SELECT *
FROM users
WHERE role='admin'
OR 'abc'='abc'
"""


bad_query3 = """
SELECT *
FROM users
WHERE id=2
OR 999=999
"""


message = """
SELECT is used to retrieve data
"""


table_name = "users"


normal_text = (
    "UPDATE documentation"
)

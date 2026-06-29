username = input()

query = "SELECT * FROM users WHERE username='" + username + "'"

cursor.execute(query)

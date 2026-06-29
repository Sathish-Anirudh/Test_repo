user_id = input("Enter ID: ")

query = f"SELECT * FROM users WHERE id={user_id}"

print(query)

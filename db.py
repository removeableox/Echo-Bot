import sqlite3

connection = sqlite3.connect("main.db")
cursor = connection.cursor()
rows = cursor.execute("SELECT * FROM connections").fetchall()
print(rows)
connection.commit()

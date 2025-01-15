import sqlite3

conn = sqlite3.connect("zmatky.db")

cursor = conn.cursor()

input_color = input("Add house color:")
#zápis do databáze
cursor.execute(
    "INSERT INTO houses (color) VALUES (?)", (input_color,)
)
conn.commit()

cursor.execute("SELECT * FROM houses")
rows = cursor.fetchall()
for row in rows:
    print(row[1])

conn.close()
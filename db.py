#dummy script used to display data of my db
import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("SELECT title, rating, published_date FROM books WHERE category = 'Fiction'")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

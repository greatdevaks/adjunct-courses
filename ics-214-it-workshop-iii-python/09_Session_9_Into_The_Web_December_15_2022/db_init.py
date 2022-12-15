import sqlite3

connection = sqlite3.connect("database.db")

sql_schema_file = "posts.sql"

with open(sql_schema_file) as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ("First Post", "Content for the first post"),
)

cur.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ("Second Post", "Content for the second post"),
)

connection.commit()
connection.close()

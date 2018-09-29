import sqlite3

with sqlite3.connect("database.db", check_same_thread=False) as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User(
username VARCHAR PRIMARY KEY,
password VARCHAR);
''')

cursor.execute("SELECT * FROM User")
print(cursor.fetchall())
import sqlite3

db_name = "test.db"

conn = sqlite3.connect(db_name)

cursor = conn.cursor()

cursor.execute('''create table if not exists users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        contact TEXT,
        city TEXT
               )
''')

cursor.execute("insert into users (name,contact,city) values  (?,?,?)",('shree','8850024342','Kolhapur'))
cursor.execute("insert into users(name,contact,city) values (?,?,?)",('ram','8850024343','Pune'))

conn.commit()

cursor.execute("select * from users")
rows=cursor.fetchall()

for user in rows:
    print(f"Name:{user[1]}, Contact:{user[2]}, City:{user[3]} ")

conn.close()
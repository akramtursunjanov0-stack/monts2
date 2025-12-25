import sqlite3

# подключение к базе (создаст файл, если его нет)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# добавление данных
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alex", 16))
conn.commit()

# запрос данных
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()



















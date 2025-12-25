import sqlite3

DB_NAME = "books.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                author TEXT,
                publication_year INTEGER
            )
        """)
        conn.commit()


def add_book(name, author, publication_year):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (name, author, publication_year) VALUES (?, ?, ?)",
            (name, author, publication_year)
        )
        conn.commit()


def get_all_books():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()


def update_book_name(book_id, new_name):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE books SET name = ? WHERE id = ?",
            (new_name, book_id)
        )
        conn.commit()


def delete_book(book_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )
        conn.commit()
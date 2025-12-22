import sqlite3


def create_table():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    conn.commit()
    conn.close()
    print("Таблица books создана (или уже существует).")


def insert_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 288, 4),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Science Fiction", 249, 6),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 3),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 350, 7),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Classic", 277, 2),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 324, 4),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 5),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 671, 2),
        ("The Alchemist", "Paulo Coelho", 1988, "Philosophy", 208, 6),




    ]

    cursor.executemany("""
        INSERT INTO books (
            name, author, publication_year, genre,
            number_of_pages, number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()
    print("Книги успешно добавлены в таблицу books.")


if __name__ == "__main__":
    create_table()
    insert_books()

import  sqlite3

def create_tadles(connection):
    connection.execute("""
    CREATE TABLE stedents (
      name TEXT, 
      age INTEGER,
      city TEXT       
    )
    """)
def add_student(connection , name, age , city):
    connection.execute('''INSERT INTO student , name, age ,city ''')



if __name__ == '__main__':
    conn = sqlite3.connect('database.db')





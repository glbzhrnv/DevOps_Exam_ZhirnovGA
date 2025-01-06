import sqlite3

DATABASE = "database/e_library.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        with open("database/schema.sql", "r") as schema_file:
            conn.executescript(schema_file.read())
        with open("database/data.sql", "r") as data_file:
            conn.executescript(data_file.read())

def query_db(query, args=(), one=False):
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row 
        cur = conn.execute(query, args)
        results = cur.fetchall()
        return (results[0] if results else None) if one else results

def add_user(username, password, purchased_game):
    query = "INSERT INTO users (username, password, purchased_game) VALUES (?, ?, ?)"
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(query, (username, password, purchased_game))
        conn.commit()

def get_books():
    query = "SELECT title, author, publisher FROM books"
    return query_db(query)

def authenticate_user(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    return query_db(query, (username, password), one=True)

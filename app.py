from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретный ключ для работы сессий

def query_db(query, args=(), one=False):
    """Функция для выполнения SQL-запросов."""
    with sqlite3.connect("database/e_library.db") as conn:
        conn.row_factory = sqlite3.Row  # Используем Row factory для доступа к результатам как к словарям
        cur = conn.execute(query, args)
        rv = cur.fetchall()
        return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books():
    # Если пользователь не авторизован, показываем только название книги и автора
    books = query_db("SELECT title, author, publisher FROM books")
    
    if 'user_id' not in session:  # Не авторизованный пользователь
        return render_template('books.html', books=[{"title": b['title'], "author": b['author']} for b in books])
    
    # Для авторизованных пользователей показываем книги с издательствами и взятыми книгами
    borrowed_books = query_db("""
        SELECT b.title, b.author, b.publisher, bb.borrow_date, bb.return_date 
        FROM borrowed_books bb
        JOIN books b ON bb.book_id = b.id
        WHERE bb.user_id = ?
    """, (session['user_id'],))

    return render_template('books.html', books=[{"title": b['title'], "author": b['author'], "publisher": b['publisher']} for b in books], borrowed_books=borrowed_books)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = query_db("SELECT * FROM users WHERE username = ? AND password = ?", 
                        (data['username'], data['password']), one=True)
        if user:
            session['user_id'] = user['id']  # Сохраняем user_id в сессии
            return redirect(url_for('get_books'))  # Перенаправляем на страницу с книгами
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/borrowed_books', methods=['GET'])
def get_borrowed_books():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Перенаправление на страницу логина, если пользователь не авторизован
    
    user_id = session['user_id']
    borrowed_books = query_db("""
        SELECT b.title, b.author, b.publisher, bb.borrow_date, bb.return_date 
        FROM borrowed_books bb
        JOIN books b ON bb.book_id = b.id
        WHERE bb.user_id = ?
    """, (user_id,))
    
    return render_template('borrowed_books.html', borrowed_books=borrowed_books)

if __nome__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

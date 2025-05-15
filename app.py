from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages
conn = sqlite3.connect('books.db', check_same_thread=False)

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

# Signup Route
# ------------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        phone = request.form['phone']

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('signup.html', name=name, email=email, phone=phone)

        try:
            conn = sqlite3.connect('books.db')
            c = conn.cursor()
            c.execute('''
                INSERT INTO users (name, gender, email, password, phone)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, gender, email, password, phone))
            conn.commit()
            conn.close()

            flash('You have registered successfully. Now please login to continue.', 'success')
            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            flash('An account with this email already exists.', 'error')
            return render_template('signup.html', name=name, email=email, phone=phone)

    return render_template('signup.html')


# ------------------------------
# Login Route
# ------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('books.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')
            return render_template('login.html', email=email)

    return render_template('login.html')

@app.route('/find_books', methods=['POST'])
def find_books():
    category = request.form.get('genre')
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books WHERE category = ?', (category,)).fetchall()
    conn.close()

    # If the request was sent via JavaScript fetch(), return JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify([dict(row) for row in books])

    return render_template('index.html', books=books)



# ------------------------------
# Home Route
# ------------------------------
@app.route('/')
def home():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', books=books)

# ------------------------------
# Add Book Route
# ------------------------------
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']

        conn = sqlite3.connect('books.db')
        c = conn.cursor()
        c.execute("INSERT INTO books (title, author, category) VALUES (?, ?, ?)", (title, author, category))
        conn.commit()
        conn.close()

        flash('Book added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('add_book.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))


# ------------------------------
# Run App
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)

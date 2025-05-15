from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("books.db", check_same_thread=False)


def get_db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row
    return conn


# Signup Route
# ------------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        phone = request.form["phone"]

        if password != confirm_password:

            return render_template("signup.html", name=name, email=email, phone=phone)

        try:
            conn = sqlite3.connect("books.db")
            c = conn.cursor()
            c.execute(
                """
                INSERT INTO users (name, gender, email, password, phone)
                VALUES (?, ?, ?, ?, ?)
            """,
                (name, gender, email, password, phone),
            )
            conn.commit()
            conn.close()

           

        except sqlite3.IntegrityError:
          
            return render_template("signup.html", name=name, email=email, phone=phone)

    return render_template("signup.html")


# ------------------------------
# Login Route
# ------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
        )
        user = c.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]
            session["user_name"] = user[1]

            return redirect(url_for("home"))
        else:
          
            return render_template("login.html", email=email)

    return render_template("login.html")


@app.route("/find_books", methods=["POST"])
def find_books():
    category = request.form.get("category")
    if not category:
        return "No category provided", 400

    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT title, author, rating, published_date, description FROM books WHERE category=?",
        (category,),
    )
    rows = cursor.fetchall()
    conn.close()

    print(
        f"📘 Fetching books for category: {category} - {len(rows)} found"
    )  # 👈 Debug print

    books = []
    for row in rows:
        books.append(
            {
                "title": row[0],
                "author": row[1],
                "rating": row[2],
                "published_date": row[3],
                "description": row[4],
            }
        )

    # Handle AJAX request
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return jsonify(books)

    # Or render the same index.html with filtered books
    return render_template("index.html", books=books)


# ------------------------------
# Home Route
# ------------------------------
@app.route("/")
def home():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template("index.html", books=books)


# ------------------------------
# Add Book Route
# ------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        published_date = request.form["published_date"]
        description = request.form["description"]
        category = request.form["category"]

        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        c.execute("""
            INSERT INTO books (title, author, published_date, description, category)
            VALUES (?, ?, ?, ?, ?)
        """, (title, author, published_date, description, category))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))

    return render_template("add_book.html")

@app.route("/logout")
def logout():
    session.clear()
    
    return redirect(url_for("login"))


# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)

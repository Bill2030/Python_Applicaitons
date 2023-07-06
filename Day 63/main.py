from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), Movie())
    rating = db.Column(db.Float, nullable=False)

    def __init__(self, id, title, author, rating):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

    def __repr__(self):
        return f'{self.title}'


with app.app_context():
    db.create_all()
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)


with app.app_context():
    db.session.commit()
    books = Book.query.all()

for book in books:
    print(book.title)
    print(book.author)



# db = sqlite3.connect('books_collection.db')
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,"
# "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO Books VALUES(1, 'Harry Porter','jk Rolling', '9.3')")
# db.commit()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book =Book (
            title= request.form["title"],
            author= request.form["author"],
            rating= request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
    return render_template("add.html")
    return redirect(url_for("home"))







if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002)

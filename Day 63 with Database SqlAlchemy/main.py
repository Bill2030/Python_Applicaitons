from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///project.db"
db.init_app(app)

class books(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200), nullable= False)
    author = db.Column(db.String(200), nullable= False)
    rating = db.Column(db.Float, unique=True)
with app.app_context():
    db.create_all()

#with app.app_context():
    #result = db.session.execute(db.select(books).order_by(books.title))
    #all_books = books.scalars()
    #new_book = books(title= "Harry Porter", author="jl.Rowling",rating= 4)
    #db.session.add(new_book)
    #db.session.commit()



all_books = []


@app.route('/')
def home():
    return render_template('index.html', books = all_books)


@app.route("/add" ,methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, port= 5002, host="127.0.0.1")


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///project.db"
db.init_app(app)

class books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable= False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, Unique= True)

with app.app_context():
    db.create_all()



#conn = pyodbc.connect('Driver={SQL Server};'
                      #'Server=DESKTOP-I3AL5H5;'
                      #'Database=MFI-RWANDA;'
                      #'Trusted_Connection=yes;')
#cursor = conn.cursor()
#cursor.execute('SELECT * FROM CLIENT')
#for i in cursor:
    #print(i)

db = sqlite3.connect('books-collection.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT OR REPLACE INTO books VALUES(1,'Harry Porter', 'J.K Rowling', '9.3')")
db.commit()
all_books = []


@app.route('/')
def home():
    return render_template("index.html", books= all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002, host="127.0.0.1")


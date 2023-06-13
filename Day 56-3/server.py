from flask import Flask
from flask import render_template
from datetime import *



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


    year = datetime.now()
    current_year = year.year




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)



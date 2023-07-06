from flask import Flask
from flask import render_template, url_for, redirect
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1> name:{name}, password:{password}</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002)

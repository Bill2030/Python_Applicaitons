from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from markupsafe import Markup


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')

app = Flask(__name__)
app.secret_key = "1234"

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def receive_data():
    return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002)
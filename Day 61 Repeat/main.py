from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "Donatello123"


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=15)])
    remember = BooleanField('Remember Me')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/SignUp')
def Signup():
    return render_template('signup.html')





if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002)

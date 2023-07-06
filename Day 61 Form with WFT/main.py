from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SearchField
from wtforms.validators import DataRequired, length

app = Flask(__name__)
app.secret_key = 'key'


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField("log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', '  POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == " admin@email.com" and login_form.password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5002)

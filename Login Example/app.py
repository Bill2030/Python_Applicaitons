from flask import Flask, flash, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = "thisisthescret"

@app.route('/')
def index():
    return render_template("index.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002)

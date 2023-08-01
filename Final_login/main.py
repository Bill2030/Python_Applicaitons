from flask import Flask, render_template, url_for, redirect, request, session
import pyodbc, re, hashlib


app = Flask(__name__)
app.secret_key= "secret"

conn = pyodbc.connect('Driver={SQl Server};'
                      'Server=DESKTOP-I3AL5H5;'
                      'Database=MFI-RWANDA;'
                      'Trusted_connection=Yes')

@app.route('/')
def login():
    if request.method == "POST" and 'username' in request.form and 'password'in request.form:
        username = request.form['username']
        password = request.form['password']
        #Retrieve the Hashed Password
        hash = password + app.secret_key
        hash = hashlib.sha1(hash.encode())
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM _rtblAgents where username = %s AND password = %s', (username, password))
        #Fetch one record and return result
        account = cursor.fetchone()
        #if account exists:
        if account:
            #Create a session data, we can access this data in other routes
            session['loggedin'] = True
            session['id']= account['id']
            session['username']= account['username']
            #Redirect to Home Page
            return 'Logged in Successfully'
        else:
            msg = 'Incorrect Username or Password'


    return render_template("index.html", msg='')

if __name__=="__main__":
    app.run(debug=True, port=5002, host="127.0.0.1")


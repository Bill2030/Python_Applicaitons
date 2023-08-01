from flask import Flask, render_template, url_for, redirect, request
import pyodbc


app = Flask(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-I3AL5H5;'
                      'Database=MFI-MAROC;'
                      'Trusted_connection=Yes')


@app.route('/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username= request.form.get("username")
        password = request.form.get("password")
        cursor = conn.cursor()
        cursor.execute('SELECT CAGENTNAME, CPASSWORD FROM _rtblAgents')

    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True, port=5002, host="127.0.0.1")
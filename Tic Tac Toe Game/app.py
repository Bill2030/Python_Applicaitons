from flask import Flask, render_template, request
import pyodbc as py

app = Flask(__name__)
#if request.method == "POST":
conn = py.connect(
    'Driver={SQL Server};'
    'server=DESKTOP-I3AL5H5;'
    'Database=MFI-MAROC;'
    'Trusted-connection = yes;')
cursor = conn.cursor()
cursor.execute('SELECT CAGENTNAME,CPASSWORD FROM _rtblAgents WHERE IDAGENTS=1')
for name in cursor:
    print(name)



@app.route('/', methods=['POST', 'GET'])
def home():

    return render_template("index.html")

@app.route('/login', methods= ['POST', 'GET'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True, port=5002, host="127.0.0.1")





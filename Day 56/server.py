from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("bill.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5002, debug=True)


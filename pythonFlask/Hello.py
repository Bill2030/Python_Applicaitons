from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/bye')
def greeting():
    return "Bye"


#Creating variable paths and converting the path to a specified variable
@app.route("/name")
def greet(name):
    if name == "Bill":
        return f"Hello there {name}, your are 12 years old"
new = greet("Bill")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)



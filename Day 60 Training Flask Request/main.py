from flask import Flask
from flask import render_template, url_for
import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    return f'<h1>The language is: {language}</h1>'.format(language)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002)

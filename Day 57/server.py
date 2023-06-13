import datetime

from flask import Flask
from flask import render_template
from datetime import *
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now()
    year = current_year.year

    return render_template("index.html", num= year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name= {name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, person_age=age, gender=gender)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=5002)


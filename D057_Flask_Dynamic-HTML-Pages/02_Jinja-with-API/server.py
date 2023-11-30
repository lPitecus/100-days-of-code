from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return '<p>oiee<p>'


@app.route("/guess/<name>")
def guesser_page(name):
    params = {
        'name': name
    }
    gender_response = requests.get("https://api.genderize.io", params=params)
    age_response = requests.get("https://api.agify.io", params=params)
    gender = gender_response.json()['gender']
    age = age_response.json()['age']
    return render_template("index.html", nome=name.title(), gen=gender, idade=age)


if __name__ == '__main__':
    app.run(debug=True)

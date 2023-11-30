from flask import Flask
import random
app = Flask(__name__)

number = random.randint(0, 9)


@app.route("/")
def home_page():
    return ('<h1>Welcome!! Guess a number from 0 to 9</h1>'
            '<img src="https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif"/>')

@app.route("/<guess>")
def check_result(guess):
    if int(guess) == number:
        return ('<h1>You got it right!!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>')
    if int(guess) > number:
        return ('<h1>Too high!! Try again.<h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>')
    if int(guess) < number:
        return ('<h1>Too low!! Try again.<h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>')


if __name__ == '__main__':
    print(number)
    app.run(debug=True)
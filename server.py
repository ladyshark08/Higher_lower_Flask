from flask import Flask
from random import randint

app = Flask(__name__)

correct_number = randint(1, 9)
print(correct_number)


@app.route("/")
def homepage():
    return ("<h1>Guess a number between 0 and 9</h1> <img "
            "src='https://media.giphy.com/media/v1"
            ".Y2lkPTc5MGI3NjExdnYxeTJldmx2bTBsbTY1N2w2dDEzazV1Ymk4MDExYmZ3dGFub2JoOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:number>")
def check_answer(number):
    if number == correct_number:
        return ("<h1 style='color: purple'> You found me </h1> <img "
                "src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif number > correct_number:
        return ("<h1 style='color: blue'> Too high, try again! </h1> <img "
                "src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif number < correct_number:
        return ("<h1 style='color: red'> Too low, try again! </h1> <img "
                "src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")


app.run(debug=True)

#!/usr/bin/python3
"""
Starts a flask application
This web application is listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
replacing all underscore with a space
/python/<text>: display “Python ”, followed by the value of the text variable
replacing all underscore with a space
/number/<n>: displays 'n is a number' only if n is an integer

"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_h():
    """ Method that displays 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """ Method that displays 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Displays 'C' and then the value of <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_p_text(text="is cool"):
    """Displays 'Python' and then the value of <text> """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Method that displays 'n' only if it is an integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

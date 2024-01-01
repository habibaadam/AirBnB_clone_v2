#!/usr/bin/python3
"""
Starts a flask application
This web application is listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
replacing all underscore with a space
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

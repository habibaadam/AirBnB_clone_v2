#!/usr/bin/python3
"""A script that sets up a flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes the current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def show_state():
    """Displays an HTML page with a list of all States in DBStorage"""
    state = storage.all(State)
    return render_template('9-states.html', state=state)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """displays an html page based on the state id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

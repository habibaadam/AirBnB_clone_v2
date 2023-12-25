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
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """list the cities of the state id specified"""
    myList = [obj for obj in storage.all("State").values()
              if obj.id == escape(id)]
    if len(myList) == 1:
        state = myList[0]
    else:
        state = None
    return render_template("9-states.html", state_id=id, state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

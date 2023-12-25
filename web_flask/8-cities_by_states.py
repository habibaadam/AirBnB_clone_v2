#!/usr/bin/python3
"""A script that sets up a flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes the current SQLAlchemy session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """Displays an HTML page with a list of all States with related cities
    in DBStorage
    """
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda st: st.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""import"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities():
    """variable"""
    state = storage.all(State).values()
    return render_template("8-cities_by_states.py", states=state)


@app.teardown_appcontext
def close(error):
    """return"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

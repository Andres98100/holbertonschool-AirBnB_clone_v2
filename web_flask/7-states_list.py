#!/usr/bin/python3
"""import flask and models"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """variable show the list"""
    state = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=state)


@app.teardown_appcontext
def close_db(error):
    """close"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

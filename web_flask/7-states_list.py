#!/usr/bin/python3
"""import"""
from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """variable"""
    state = storage.all(State).values()
    """return"""
    return render_template("7-states_list.html", state=state)


@app.teardown_appcontext
def close_db():
    """storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

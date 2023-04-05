#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
"""decorate"""
@app.route('/', strict_slashes=False)
def hello():
    """return"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"
"""decorate"""
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """return"""
    text = text.replace("_", " ")
    return f"C {text}"
"""decorate"""
@app.route("/python/", defaults={"text": "is_cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """return"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)
"""decorate"""
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return"""
    return f"{n} is a number"


if __name__ == "__main__":
    """run flask"""
    app.run(host="0.0.0.0", port=5000)

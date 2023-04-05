#!/usr/bin/python3
"""import"""
from flask import Flask
"""conector"""


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


"""entry point"""
if __name__ == "__main__":
    """run flask"""
    app.run(host="0.0.0.0", port=5000)

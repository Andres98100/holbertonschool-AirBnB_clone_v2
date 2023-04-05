#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""decorate"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return"""
    return 'Hello HBNB!'
"""decorate"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

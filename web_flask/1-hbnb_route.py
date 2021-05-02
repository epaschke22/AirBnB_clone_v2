#!/usr/bin/python3
""" Flask Task """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns message with no path"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns message with path"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host="0.0.0.0")

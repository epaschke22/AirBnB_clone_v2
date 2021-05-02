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

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """returns mssage as path argument"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is_cool"):
    """returns message with default path value"""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0")

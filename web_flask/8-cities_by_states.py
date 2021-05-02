#!/usr/bin/python3
""" Flask Task """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.state import City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """returns html with cities listed per state"""
    all_states = storage.all(State)
    all_cities = storage.all(City)
    return render_template('8-cities_by_states.html', States=all_states)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

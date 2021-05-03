#!/usr/bin/python3
""" Flask Task """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_id(id=None):
    """returns html with state id and cities in that state"""
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', States=all_states,
                           Amenities=all_amenities)


@app.teardown_appcontext
def teardown(self):
    """closes up the storage object"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
""" Flask Task """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.state import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """returns html with list of states"""
    all_states = storage.all(State)
    return render_template('9-states.html', States=all_states, ID=None,
                           Stateobj=None)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """returns html with state id and cities in that state"""
    all_states = storage.all(State)
    foundstate = None
    for key, state in all_states.items():
        if state.id == id:
            foundstate = state
            break

    return render_template('9-states.html', States=all_states, ID=id,
                           Stateobj=foundstate)


@app.teardown_appcontext
def teardown(self):
    """closes up the storage object"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
""" Flask Task """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """returns html with state list"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', States=all_states)


@app.teardown_appcontext
def teardown():
    """closes up the storage object"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")

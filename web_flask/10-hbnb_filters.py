#!/usr/bin/python3

from models import storage
from flask import flask
from flask import render_template

app = Flask(__name__)

# Define the route for '/states' and specify
#	strict_slashes=False to handle trailing slashes
@app.route("/states", strict_slashes=False)
def states():
	"""Displays an HTML page with a list of all States.

	Staes are sorted by name.
	"""
	# Fetch all State Objects from the
	#	Storage (FileStorage or DBStorage)
	states = storage.all("State")

	# Render the "9-states.html" template and
	#	pass the list of states as the variable 'state'
	return render_template("9-states.html", state=states)

# Define the route for '/states/<id>' and
#	specify strict_slashes=False to handle trailing slashes
@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
	"""Displays an HTML page with with info about <id>, if it exists."""

	# Loop thrugh all state objects in
	#	the storage (FileStorage of DBStorage)
	for state in storage.all("State").values():
		# check if the current state object's id matches the requested <id>
		if state.id == id:
			# if a matching state is found,
			#	render the "9-states.html" template and pass the state object
			return render_template("9-states.html)


# Teardown app context to remove
#	the current SQLAIchemy session after each request
@app.teardown_appcontext
def teardown(exc):
	"""Remove the current SQLAIchemy session."""
	storage.close()


if __name__ == "__main__":
	# Start the Flask development server
	# Listen on all available network interfaces (0.0.0.0) and port 5000
	app.run(host="0.0.0.0")

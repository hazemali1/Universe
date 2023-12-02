#!/usr/bin/python3
from flask import Flask, render_template
from functions import api_universe
from functions import api_details


app = Flask(__name__)



@app.route('/', strict_slashes=False)
def api():
	universe = api_universe()
	details = api_details()
	return render_template('index.html', universe=universe, details=details)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5009)

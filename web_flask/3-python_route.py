#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__main__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'."""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.
    replaces any underscores in <text> with spaces"""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'python' followed by the value <text>
    Replaces any underscores in <text> with spaces"""
    text = text.replace("_", " ")
    return "python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

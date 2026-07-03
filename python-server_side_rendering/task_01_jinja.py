#!/usr/bin/python3
"""Basic Flask app rendering a template."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render index page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
#!/usr/bin/env python3
"""
basic flask app
"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    """
    index function
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

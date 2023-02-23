#!/usr/bin/env python3
"""
basic flask app1
"""
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["GET"])
def index():
    """
    index function
    """
    current_time = datetime.now().strftime("%b %d, %Y, %I:%M:%S %p")
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

#!/usr/bin/env python3
"""
basic flask app1
"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config:
    """class cofig for the Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"])
def index():
    """
    index function
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

#!/usr/bin/env python3
"""
Basic Flask App 4
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import locale

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config:
    """
    Class config for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get the best matching language based on accept headers and URL param locale
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale

    # Check if URL parameter locale is supported and return it
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """
    Set the user's locale based on URL param locale
    """
    if request.args.get('locale') in app.config['LANGUAGES']:
        g.user = type(
            'User', (object,), {
                'locale': request.args.get('locale')})


@app.route('/', methods=['GET'])
def index():
    """
    Index function
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

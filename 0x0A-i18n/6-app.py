#!/usr/bin/env python3
"""
Flask app that takes in a URL parameter and renders a template
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configuration class for Babel object
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user dictionary based on the user ID provided in the URL parameter,
    or None if the user ID is not found or if the login_as parameter is not provided.
    """
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@babel.localeselector
def get_locale():
    """
    Determines the user's locale preference based on the URL parameter, the user's
    preferred locale if it is supported, the request header, or the default locale.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    user = get_user()
    if user and user['locale'] and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    header_locale = request.headers.get('locale')
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale

    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    """
    Executed before all other functions. Sets the g.user object to the current user dictionary.
    """
    g.user = get_user()


@app.route('/')
def hello_world():
    """
    Render a template with a welcome message, using the user's preferred locale if available.
    """
    welcome_message = gettext('You are not logged in.')
    if g.user:
        welcome_message = gettext('You are logged in as %(username)s.', username=g.user['name'])
    return render_template('6-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run()

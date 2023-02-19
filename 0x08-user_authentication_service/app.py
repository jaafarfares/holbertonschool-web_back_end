#!/usr/bin/env python3
"""flask app
"""
from flask import *
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def index():
    """
    basic flask app
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    register user app
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    login user app
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id, secure=True, httponly=True)
        return response
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
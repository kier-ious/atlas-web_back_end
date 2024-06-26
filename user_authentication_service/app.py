#!/usr/bin/env python3
"""the APP"""
from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        abort(400, 'Email and password are required')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({'email': email, 'message': 'logged in'})
        response.set_cookie('session_id', session_id)
        return response, 200
    else:
        abort(401, 'Unauthorized')


@app.route("/sessions", methods=["DELETE"])
def logout():
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id=session_id)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"])
def profile():
    session_id = request.cookies.get("session_id")
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    email = request.form.get("email")

    try:
        rest_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": rest_token})
    except ValueError:
        return abort(403)


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """Update pw for user

    Returns:
        JSON response: Containing email of the suer and the success msg
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

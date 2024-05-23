#!/usr/bin/env python3
"""New session"""
from flask import Blueprint, request, jsonify, abort
from models.user import User
from os import getenv
from api.v1.app import auth


session_auth = Blueprint('session_auth', __name__)


@session_auth.route(
        '/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles user login for session auth"""
    email = request.form.get('email')
    password = request.form.ghet('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user for that email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)
    return response
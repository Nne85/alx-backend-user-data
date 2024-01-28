#!/usr/bin/env python3
""" Module of Users views
"""
import os
from api.v1.views import app_views
from models.user import User
from flask import jsonify, request


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth():
    """_summary_
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            resp.set_cookie(session_name, session_id)
            return resp
    return jsonify({"error": "wrong password"}), 401

    def logout():
        """for logging out user """
        from api.v1.app import auth
        if auth.destroy_session(request):
            return jsonify({}), 200
            abort(404)

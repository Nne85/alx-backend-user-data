#!/usr/bin/env python3
"""
auth module
"""
import os
from flask import request
from typing import List, TypeVar


class Auth:
    """
    authenticate
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"
        path that require authentication

        Args:
            path: path that require authentication

            excluded_paths: path that dont require auth

        returns: False
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        """
        if request is None:
            return None

        header = request.headers.get('Authorization')

        if header is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        get current user
        """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)

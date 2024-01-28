#!/usr/bin/env python3
"""
basic_auth module
"""
import base64
import binascii
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Inherits from Auth class """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for
        Basic Authentication.

        Args:
        - authorization_header (str): The Authorization header.

        Returns:
        - str: The Base64 part of the Authorization header or None.
        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string.

        Args:
        - base64_authorization_header (str): The Base64 string to decode.

        Returns:
        - str: The decoded value as a UTF-8 string or None.
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except base64.binascii.Error:
            return None

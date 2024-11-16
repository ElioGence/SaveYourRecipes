# backend/utils/auth_utils.py

import jwt
from datetime import datetime, timedelta
from flask import current_app
from flask_jwt_extended import decode_token, get_jwt_identity, verify_jwt_in_request

def generate_jwt(user_id):
    """
    Generate a JWT token with user_id as identity and an expiration time.
    """
    expiration_time = timedelta(hours=1)  # Token expiration time (1 hour)
    access_token = jwt.encode(
        {'sub': user_id, 'exp': datetime.utcnow() + expiration_time},
        current_app.config['SECRET_KEY'],  # Secret key from Flask config
        algorithm='HS256'
    )
    return access_token

def decode_jwt(token):
    """
    Decode a JWT token to extract the identity (user_id) and check its validity.
    """
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']  # Return user_id from the token
    except jwt.ExpiredSignatureError:
        raise ValueError('Token has expired')
    except jwt.InvalidTokenError:
        raise ValueError('Invalid token')

def get_current_user():
    """
    Retrieve the current user_id from the JWT token.
    This function assumes that the token is already present in the request header.
    """
    try:
        verify_jwt_in_request()  # Ensure the JWT is valid
        return get_jwt_identity()  # Return the identity (user_id) from the JWT
    except Exception as e:
        raise ValueError("User not authenticated: " + str(e))

def check_token_validity(token):
    """
    Check if the JWT token is valid (not expired or tampered with).
    """
    try:
        decode_jwt(token)  # Try to decode the token and check its validity
        return True
    except ValueError:
        return False

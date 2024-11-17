from flask import Blueprint, request, jsonify
from utils.auth_utils import generate_jwt 

users_routes = Blueprint('users_routes', __name__)

# Login route to generate JWT token
@users_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Simulate user verification (replace with actual DB logic)
    if username == 'testuser' and password == 'testpassword':
        # Generate JWT Token (you can also use `generate_jwt()` function here)
        user_id = 1  # Replace with the actual user ID after validation
        access_token = generate_jwt(user_id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# More user-related routes (e.g., signup, logout) can go here...

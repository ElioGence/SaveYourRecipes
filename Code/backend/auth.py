from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import user, db

auth_bp = Blueprint('auth', __name__)

# Example login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if not username or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Check if the user already exists
    if user.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 409

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = user(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

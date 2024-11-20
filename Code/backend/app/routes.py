from .models import Recipe, User, db
from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin

main_bp = Blueprint('main', __name__)

@main_bp.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

@main_bp.route('/signup', methods=['POST', 'OPTIONS'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])  
def signup():
    if request.method == 'OPTIONS':
        # Preflight request handling
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response

    # Process the signup request
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@main_bp.route('/login', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])  
def login():
    # Get the username and password from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Find the user with the given username
    user = User.query.filter_by(username=username).first()

    # Check if the user exists and if the password matches
    if user and user.password == password:
        return jsonify({"message": "Login successful", "user_id": user.id}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@main_bp.route('/recipes', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])  
def get_recipes():
    user_id = request.args.get('user_id')  # Get user_id from query parameters
    if not user_id:
        return jsonify({"message": "user_id is required"}), 400
    
    recipes = Recipe.query.filter_by(user_id=user_id).all()  # Assuming user_id is used to filter recipes
    return jsonify([recipe.to_dict() for recipe in recipes])

@main_bp.route('/recipes', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])  
def add_recipe():
    data = request.json
    new_recipe = Recipe(name=data['name'], description=data['description'], link=data['link'], user_id=data['user_id'])
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify(new_recipe.to_dict()), 201



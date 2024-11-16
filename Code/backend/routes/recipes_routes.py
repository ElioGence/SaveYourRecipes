from flask import Blueprint, request, jsonify
from backend.utils.auth_utils import generate_jwt  # Example of importing utility

recipe_routes = Blueprint('recipe_routes', __name__)
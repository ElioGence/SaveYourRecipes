from flask import Flask
from flask_jwt_extended import JWTManager
import os

# Initialize the JWTManager instance
jwt = JWTManager()

def create_app(config_name):
    # Create the Flask app
    app = Flask(__name__)

    # Load configuration from environment or .env file
    app.config['SECRET_KEY'] = os.getenv('FLASK_APP_SECRET_KEY')  # For session management
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # For JWT tokens
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Database URL
    
    # Initialize extensions
    jwt.init_app(app)

    # Register routes
    app.register_blueprint(recipe_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(ingredients_routes)
    app.register_blueprint(recipe_ingredients_routes)

    return app

@app.route('/')
def home():
    return "Hello, Recipe Manager!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


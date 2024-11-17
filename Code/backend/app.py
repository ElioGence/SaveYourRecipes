from flask import Flask
from flask_jwt_extended import JWTManager
import os
from routes.recipes_routes import recipes_routes  
from routes.users_routes import users_routes 
from routes.ingredients_routes import ingredients_routes  
from routes.recipe_ingredients_routes import recipe_ingredients_routes  

# Initialize the JWTManager instance
jwt = JWTManager()

def create_app(config_name):
    # Create the Flask app
    app = Flask(__name__)

    # Load configuration from environment or .env file
    if config_name == 'development':
        app.config['SECRET_KEY'] = os.getenv('FLASK_APP_SECRET_KEY')  # For session management
        app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  # For JWT tokens
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Database URL
        app.config['DEBUG'] = True

    # Initialize extensions
    jwt.init_app(app)

    # Register routes
    app.register_blueprint(recipes_routes)
    app.register_blueprint(users_routes)
    app.register_blueprint(ingredients_routes)
    app.register_blueprint(recipe_ingredients_routes)

    return app

if __name__ == "__main__":
    config_name = os.getenv('FLASK_ENV', 'development')
    app = create_app('development')
    app.run(host="0.0.0.0", port=5000)

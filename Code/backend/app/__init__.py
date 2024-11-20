from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS  # Import CORS
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Enable CORS for all routes
    CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

    # Register Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

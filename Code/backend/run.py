from app import create_app 
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get Flask environment from .env or default to 'development'
flask_env = os.getenv("FLASK_ENV", "development")

# Create the app instance using the environment setting
app = create_app(flask_env)

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)

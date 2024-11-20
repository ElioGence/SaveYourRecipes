import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

print(f"DATABASE_URL: {os.getenv('DATABASE')}")
print(f"SECRET_KEY: {os.getenv('SECRET_KEY')}")

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE', 'postgresql://username:password@localhost/recipemanager')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

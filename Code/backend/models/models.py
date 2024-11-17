from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # Store hashed password

    # Define the relationship with the recipes
    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

# Recipe Model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredients = db.relationship('Ingredient', secondary='recipe_ingredient', lazy='subquery',
                                  backref=db.backref('recipes', lazy=True))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Foreign key to User

    def __repr__(self):
        return f'<Recipe {self.name}>'

# Ingredient Model
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Ingredient {self.name}>'

# Association Table for Recipe-Ingredient (Many-to-Many Relationship)
class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredient'

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    quantity = db.Column(db.String(100), nullable=True)

    # Define relationships
    recipe = db.relationship(Recipe, backref=db.backref('recipe_ingredients', cascade='all, delete-orphan'))
    ingredient = db.relationship(Ingredient, backref=db.backref('recipe_ingredients', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'<RecipeIngredient {self.recipe_id} - {self.ingredient_id}>'

from utils.db_utils import get_db_connection
from models import User, Recipe, Ingredient, RecipeIngredient

db = get_db_connection()

# Example to add a user
new_user = User(username="john_doe", email="john.doe@example.com", password=generate_password_hash("password"))
db.session.add(new_user)
db.session.commit()

# Example to add a recipe
new_recipe = Recipe(name="Tomato Soup", description="A simple tomato soup recipe", user_id=new_user.id)
db.session.add(new_recipe)
db.session.commit()

# Example to add ingredients
ingredient1 = Ingredient(name="Tomato", quantity="5")
ingredient2 = Ingredient(name="Salt", quantity="1 tsp")
db.session.add_all([ingredient1, ingredient2])
db.session.commit()

# Link recipe and ingredients
recipe_ingredient1 = RecipeIngredient(recipe_id=new_recipe.id, ingredient_id=ingredient1.id, quantity="5 tomatoes")
recipe_ingredient2 = RecipeIngredient(recipe_id=new_recipe.id, ingredient_id=ingredient2.id, quantity="1 tsp")
db.session.add_all([recipe_ingredient1, recipe_ingredient2])
db.session.commit()

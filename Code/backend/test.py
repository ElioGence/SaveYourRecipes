from utils.db_utils import get_db_connection
from models import user, recipe, ingredient, recipeIngredient

db = get_db_connection()

# Example to add a user
new_user = user(username="john_doe", email="john.doe@example.com", password=generate_password_hash("password"))
db.session.add(new_user)
db.session.commit()

# Example to add a recipe
new_recipe = recipe(name="Tomato Soup", description="A simple tomato soup recipe", user_id=new_user.id)
db.session.add(new_recipe)
db.session.commit()

# Example to add ingredients
ingredient1 = ingredient(name="Tomato", quantity="5")
ingredient2 = ingredient(name="Salt", quantity="1 tsp")
db.session.add_all([ingredient1, ingredient2])
db.session.commit()

# Link recipe and ingredients
recipe_ingredient1 = recipeIngredient(recipe_id=new_recipe.id, ingredient_id=ingredient1.id, quantity="5 tomatoes")
recipe_ingredient2 = recipeIngredient(recipe_id=new_recipe.id, ingredient_id=ingredient2.id, quantity="1 tsp")
db.session.add_all([recipe_ingredient1, recipe_ingredient2])
db.session.commit()

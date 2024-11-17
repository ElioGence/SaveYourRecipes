from flask import Blueprint, request, jsonify
from utils.auth_utils import generate_jwt 

recipes_routes = Blueprint('recipes_routes', __name__)

# Create a new recipe
@recipes_routes.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    instructions = data.get('instructions')
    link = data.get('link')
    ingredients = data.get('ingredients', [])

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        #Insert recipe
        cursor.execute(
            "INSERT INTO recipes (name, description, instructions, link)  VALUES (%s, %s, %s, %s) RETURNING id"
        )
        recipe_id = cursor.fetchone()[0]

        # Insert ingredients
        for ingredient in ingredients:
            cursor.execute(
                "INSERT INTO ingredients (name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
                (ingredient['name'])
            )

        # Insert recipe_ingredients
        for ingredient in ingredients:
            cursor.execute(
                "INSERT INTO recipe_ingredients (recipe_id, name, quantity) VALUES (%s, %s, %s)",
                (recipe_id, ingredient['name'], ingredient['quantity'])
            )
        conn.commit()

        return jsonify({"message": "Recipe created", "recipe_id": recipe_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# Get all recipes
@recipes_routes.route('/recipes', methods=['GET'])
def get_recipes():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT * FROM recipes")
        recipes = cursor.fetchall()
        return jsonify(recipes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Get a single recipe (with ingredients)
@recipes_routes.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
        recipe = cursor.fetchone()
        if not recipe:
            return jsonify({"error": "Recipe not found"}), 404

        cursor.execute("SELECT * FROM recipe_ingredient WHERE recipe_id = %s", (recipe_id,))
        ingredients = cursor.fetchall()

        recipe['ingredients'] = ingredients
        return jsonify(recipe)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Update a recipe
@recipes_routes.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    instructions = data.get('instructions')
    link = data.get('link')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE recipes SET name = %s, description = %s, instructions = %s , link = %s WHERE id = %s",
            (name, description, instructions, link, recipe_id)
        )
        conn.commit()
        return jsonify({"message": "Recipe updated"})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Delete a recipe
@recipes_routes.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute("DELETE FROM recipes WHERE id = %s", (recipe_id,))
        conn.commit()
        return jsonify({"message": "Recipe deleted"})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

#INCORECT (GET INGREDIENT FROM RECIPE)
@recipes_routes.route('/recipes/ingredients', methods=['GET'])
def get_recipes_by_ingredient():
    ingredient_name = request.args.get('ingredient')
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        query = """
            SELECT r.id, r.name, r.description, r.instructions, r.link
            FROM recipes r
            JOIN recipe_ingredients ri ON r.id = ri.recipe_id
            JOIN ingredients i ON ri.ingredient_name = i.name
            WHERE i.name = %s
        """
        cursor.execute(query, (ingredient_name,))
        recipes = cursor.fetchall()
        return jsonify(recipes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

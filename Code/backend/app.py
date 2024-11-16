from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="db",  # Name of the service in docker-compose.yml
        database="recipemanager",
        user="executiveChef",
        password="fdhsqifhmezian123+*/"
    )
    return conn

# Create a new recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():


# Get all recipes
@app.route('/recipes', methods=['GET'])
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
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        query = "SELECT * FROM recipes WHERE id="+recipe_id
        cursor.execute(query)
        #cursor.execute("SELECT * FROM recipes WHERE id = %s", (recipe_id,))
        recipe = cursor.fetchone()
        if not recipe:
            return jsonify({"error": "Recipe not found"}), 404

        cursor.execute("SELECT * FROM ingredients WHERE recipe_id = %s", (recipe_id,))
        ingredients = cursor.fetchall()

        recipe['ingredients'] = ingredients
        return jsonify(recipe)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Update a recipe
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):

# Delete a recipe
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
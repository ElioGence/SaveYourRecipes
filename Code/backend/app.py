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
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
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
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
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

# Insert an ingredient 
@app.route('/ingredients/<string:ingredient_name>', methods=['POST']) 
def add_ingredient(ingredient_name):
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Insert into ingredients (upsert logic)
        cursor.execute(
            "INSERT INTO ingredients (name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
            (ingredient_name,)
        )
        conn.commit()
        return jsonify({"message": "Ingredient added"}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# Update an ingredient 
@app.route('/ingredients/<string:ingredient_name>', methods=['PUT'])
def update_ingredient(ingredient_name):
    data = request.get_json()
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE ingredients SET name = %s WHERE name = %s",
            (name, ingredient_name)
        )
        conn.commit()
        return jsonify({"message": "Ingredient updated"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# Delete an ingredient 
@app.route('/ingredients/<string:ingredient_name>', methods=['DELETE'])
def delete_ingredient(ingredient_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM ingredients WHERE name = %s ",
            (ingredient_name)
        )
        conn.commit()
        return jsonify({"message": "Ingredient deleted"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


# Delete an ingredient from a recipe
@app.route('/recipes/<int:recipe_id>/recipe_ingredients/<string:ingredient_name>', methods=['DELETE'])
def delete_recipe_ingredient(recipe_id, ingredient_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM recipe_ingredients WHERE recipe_id = %s AND ingredient_name = %s",
            (recipe_id, ingredient_name)
        )
        conn.commit()
        return jsonify({"message": "Ingredient deleted from recipe"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/recipes/ingredients', methods=['GET'])
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


@app.route('/')
def home():
    return "Hello, Recipe Manager!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
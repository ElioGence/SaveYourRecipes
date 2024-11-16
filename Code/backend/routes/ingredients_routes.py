from flask import Blueprint, request, jsonify
from backend.utils.auth_utils import generate_jwt 

recipe_routes = Blueprint('ingredients_routes', __name__)

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
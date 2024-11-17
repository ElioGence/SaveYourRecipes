from flask import Blueprint, request, jsonify
from utils.auth_utils import generate_jwt 
from utils.db_utils import get_db_connection

recipe_ingredients_routes = Blueprint('recipe_ingredients_routes', __name__)

# Delete an ingredient from a recipe
@recipe_ingredients_routes.route('/recipes/<int:recipe_id>/recipe_ingredients/<string:ingredient_name>', methods=['DELETE'])
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
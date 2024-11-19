-- Create Recipes Table
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    link TEXT
);


-- Create RecipeIngredients Table (Join Table)
CREATE TABLE recipe_ingredients (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient VARCHAR(255),
    quantity VARCHAR(255),
    PRIMARY KEY (recipe_id, ingredient_id)
);


-- Create Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);



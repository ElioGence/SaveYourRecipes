-- Create Recipes Table
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT NOT NULL,
    link TEXT
);

-- Create Ingredients Table
CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);



-- Create RecipeIngredients Table (Join Table)
CREATE TABLE recipe_ingredients (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id VARCHAR(255) REFERENCES ingredients(id) ON DELETE CASCADE,
    quantity VARCHAR(255),
    PRIMARY KEY (recipe_id, ingredient_id)
);


-- Create Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);



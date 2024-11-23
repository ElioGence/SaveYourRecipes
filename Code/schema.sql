CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
); -- Change to add more basic information (pp, email, pseudo != name, maybe adress so that we can show market near him)

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    link TEXT, --Maybe rename to source
    /* Add image or images/video depending of the 
       Labels here, or in a seperate table (like limited in number and shared by everyone), custom type maybe ?
       Instruction (step by step)
       For how many people is it
    */
);

CREATE TABLE ingredients (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE,
    name VARCHAR(255),
    quantity INT,
    unity VARCHAR(255),
    PRIMARY KEY (recipe_id, name)
);

CREATE TABLE shared_Recipes (
    recipe_id INT REFERENCES recipes(id) ON DELETE CASCADE
    original_user_id INT REFERENCES users(id) ON DELETE CASCADE,
    shared_user_id INT REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, original_user_id, shared_user_id)
);

CREATE TABLE shopping_list (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    ingredient VARCHAR(255),
    quantity VARCHAR(255),
    date VARCHAR(255),
    shop VARCHAR(255)
);

--MEAL PLAN TABLE (1 by person BUT can be shared)


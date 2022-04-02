-- Create a new database.

CREATE DATABASE anas_restaurant;

# Use current databse
USE anas_restaurant;

-- Create new tables for database and establish relationships..

CREATE TABLE restaurant (
  id INT PRIMARY KEY,
  name VARCHAR(20),
  description VARCHAR(100),
  rating DECIMAL,
  telephone CHAR(10),
  hours VARCHAR(100)
);

# Checking if primary key was set.
SELECT 
  constraint_name, column_name, table_name
FROM
  information_schema.key_column_usage
WHERE
  table_name = 'restaurant';

CREATE TABLE address (
  id INT PRIMARY KEY,
  street_number VARCHAR(10),
  street_name VARCHAR(20),
  city VARCHAR(20),
  state VARCHAR(15),
  google_map_link VARCHAR(50),
  # Establishing a one-to-one relationship.
  restaurant_id INT REFERENCES restaurant(id)
);

CREATE TABLE category (
  id CHAR(2) PRIMARY KEY,
  name VARCHAR(20),
  description VARCHAR(200)
  );
  
CREATE TABLE dish (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  description VARCHAR(200),
  hot_and_spicy BOOLEAN
);

CREATE TABLE review (
  id INT PRIMARY KEY,
  rating INT,
  description VARCHAR(200),
  date DATE,
  #Establishing a one-to-many relationship
  restaurant_id INT REFERENCES restaurant(id)
);

#Establishing a many-to-many relationship.
CREATE TABLE categories_dishes (
  category_id CHAR(2) REFERENCES category(id),
  dish_id INT REFERENCES dish(id),
  price DECIMAL,
  PRIMARY KEY (category_id, dish_id)
);

# Using 'EXPLAIN' to see whats in my tables so far.
EXPLAIN dish;
EXPLAIN category;
EXPLAIN address;
EXPLAIN restaurant;
EXPLAIN review;

-- Insert values into the tables.
INSERT INTO restaurant VALUES (
  1, 'Anas Restaurant', 'Homecooked Goodies', 9.9, '6175551212', 'Mon - Fri 9:00 am to 5:00 pm, Weekends 09:00 am to 8:00 pm'
);

INSERT INTO address VALUES (
  1, '2022', 'Sql Street', 'Chinatown', 'London', 'https://googlemaps/AnasRestaurant', 1
);


INSERT INTO review VALUES (
  1, 8, 'Would love to come back!', '2022-01-12', 1
);

INSERT INTO review VALUES (
  2, 7, 'Just a small mix-up, other than that very good.', '2022-02-25', 1
);

INSERT INTO review VALUES (
  3, 10, 'Loveley place!', '2022-03-10', 1
);

# Ammend Review Number 1
UPDATE review SET rating = 7 WHERE review.id = 1;

INSERT INTO category VALUES (
  'BS', 'Breakfast Specials', 'Served between 09.00am and 11.00am from Monday to Sunday'
);

INSERT INTO category VALUES (
  'LS', 'Lunch Specials', 'Fresh Daily Hot Soup Served with Crunchy Bread between 11:00 am and 4:00 pm from Monday to Friday.'
);

INSERT INTO category VALUES (
  'DS', 'Dinner Specials', 'Served from 4.00pm to Closing Time from Monday to Saturday'
);

INSERT INTO dish VALUES (
  1, 'Full English Breakfast', 'A classic full english breakfast with bacon, eggs, sausages, baked beans, fried tomato, fried mushrooms, black pudding and toast.', false
);

INSERT INTO dish VALUES (
  2, 'French Toast', 'Sourdough bread dipped in a rich egg batter, served golden brown, lightly dusted with powdered sugar and served with whipped butter and hot syrup', false
);

INSERT INTO dish VALUES (
  3, 'Toastie', 'A classic ham and cheese toastie.', false
);

INSERT INTO dish VALUES (
  4, 'Fresh salmon with Thai noodle salad', 'A refreshing nutritious salmon and noodle salad containing pink salmon, peas, rice noodles topped with a slightly spicy sweet sauce', true
);

INSERT INTO dish VALUES (
  5, 'Spaghetti Carbonara', 'Homemade and fresh pasta with bacon and a creamy sauce made from eggs, parmesan and black pepper.', false
);

INSERT INTO dish VALUES (
  6, 'Tacos', 'Four soft tortilla wraps grilled and filled with beef, beans, cheese, and vegatables.', true
);

INSERT INTO dish VALUES (
  7, 'Chicken and Rice', 'Marinated chicken breast sauteed with colorful vegetables topped with pine nuts and shredded lettuce over a bed of jasmine rice.', false
);

INSERT INTO dish VALUES (
  8, 'Pizza', 'A classic pepperoni pizza', true
);

# Delete a row.
DELETE FROM dish WHERE id = 7;

INSERT INTO categories_dishes VALUES (
  'BS', 1, 6.95
);

INSERT INTO categories_dishes VALUES (
  'BS', 3, 6.95
);

INSERT INTO categories_dishes VALUES (
  'LS', 1, 8.95
);

INSERT INTO categories_dishes VALUES (
  'LS', 4, 8.95
);

INSERT INTO categories_dishes VALUES (
  'DS', 5, 8.95
);

INSERT INTO categories_dishes VALUES (
  'DS', 6, 15.95
);

INSERT INTO categories_dishes VALUES (
  'DS', 7, 16.95
);

INSERT INTO categories_dishes VALUES (
  'DS', 8, 17.95
);

# See tables with inserted data
SELECT * FROM dish;
SELECT * FROM category;
SELECT * FROM address;
SELECT * FROM restaurant;
SELECT * FROM review;

-- Querying data from the databse
# Get Restaurant name and its telephone number.
SELECT name, telephone FROM restaurant, address;

# The best rating the restaurant ever received.
SELECT rating, description FROM review WHERE rating = (SELECT MAX(rating) FROM review);

# The worst rating the restaurant ever received.
SELECT rating, description FROM review WHERE rating = (SELECT MIN(rating) FROM review);

# Get the names of the dishes and its price and which category it is from.
SELECT category.name AS category, dish.name AS dish_name, categories_dishes.price FROM category, dish, categories_dishes
WHERE categories_dishes.dish_id = dish.id AND categories_dishes.category_id = category.id
ORDER BY category.name;

# All the spicy dishes, their prices and category.
SELECT dish.name AS spicy_dish_name,
       category.name AS category,
       categories_dishes.price
FROM dish, category, categories_dishes
WHERE categories_dishes.dish_id = dish.id AND categories_dishes.category_id = category.id AND hot_and_spicy = true;

# See dishes that span multiple tables.
SELECT dish.name AS dish_name, dish_id, COUNT(dish_id) AS dish_count FROM dish, categories_dishes
WHERE dish.id = categories_dishes.dish_id
GROUP BY 1, 2 HAVING COUNT(dish_id) > 1 ORDER BY 3;

# See tables with inserted data
SELECT * FROM dish;
SELECT * FROM category;
SELECT * FROM address;
SELECT * FROM restaurant;
SELECT * FROM review;
SELECT * FROM categories_dishes;

# Join tables & Decending order
SELECT dish.name, categories_dishes.price FROM dish
INNER JOIN categories_dishes ON dish.id=categories_dishes.dish_id ORDER BY price DESC;







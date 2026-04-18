CREATE TABLE categories(
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(40)
);

CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(40),
    price INT,
    qty INT,
    category_id INT,
    FOREIGN KEY(category_id) REFERENCES categories(category_id)
ON DELETE CASCADE
);

--categories
INSERT INTO categories(category_name) VALUES('Food Products');
INSERT INTO categories(category_name) VALUES('Personal Care Products');
INSERT INTO categories(category_name) VALUES('Household Products');

--category_1
INSERT INTO products(product_name, price, qty, category_id) VALUES('Rice', 200, 50, 1);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Beans', 170, 50, 1);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Bread', 25, 15, 1);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Cooking Oil', 45, 25, 1);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Noodles', 20, 20, 1);

--category_2
INSERT INTO products(product_name, price, qty, category_id) VALUES('Soap', 6, 10, 2);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Toothpaste', 4, 12, 2);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Shampoo', 7, 5, 2);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Body Cream', 25, 15, 2);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Deodorant', 20, 20, 2);

--category_3
INSERT INTO products(product_name, price, qty, category_id) VALUES('Detergent', 4, 24, 3);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Bucket', 9, 12, 3);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Broom', 5, 5, 3);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Sponge', 4, 12, 3);
INSERT INTO products(product_name, price, qty, category_id) VALUES('Toilet Cleaner', 5, 5, 3);
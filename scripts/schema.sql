-- Drop if exists
DROP TABLE IF EXISTS inventory_logs, inventory, sale_items, sales, products, categories;

-- Categories
CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Products
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Inventory
CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    quantity INT NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Inventory Logs
CREATE TABLE inventory_logs (
    id INT PRIMARY KEY,
    product_id INT,
    quantity_change INT,
    change_type ENUM('INCREASE', 'DECREASE') NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Sales
CREATE TABLE sales (
    id INT PRIMARY KEY,
    sale_date DATETIME NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL
);

-- Sale Items
CREATE TABLE sale_items (
    id INT PRIMARY KEY,
    sale_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price_per_unit DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

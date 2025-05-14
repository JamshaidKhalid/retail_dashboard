-- Categories (id 1-20)
INSERT INTO categories (id, name, description) VALUES
(1, 'Electronics', 'Electronic gadgets and devices'),
(2, 'Books', 'Printed and digital books'),
(3, 'Clothing', 'Men and women apparel'),
(4, 'Home Appliances', 'Appliances for home use'),
(5, 'Beauty', 'Cosmetics and skincare'),
(6, 'Toys', 'Kids toys and games'),
(7, 'Automotive', 'Car accessories and parts'),
(8, 'Furniture', 'Home and office furniture'),
(9, 'Sports', 'Fitness and sports gear'),
(10, 'Grocery', 'Daily essentials and groceries'),
(11, 'Garden', 'Gardening tools and accessories'),
(12, 'Music', 'Instruments and music gear'),
(13, 'Office', 'Stationery and supplies'),
(14, 'Pets', 'Pet food and accessories'),
(15, 'Jewelry', 'Rings, necklaces, and more'),
(16, 'Footwear', 'Shoes and sandals'),
(17, 'Baby', 'Baby products'),
(18, 'Health', 'Healthcare and wellness'),
(19, 'Travel', 'Luggage and travel gear'),
(20, 'Gaming', 'Consoles and accessories');

-- Products (id 1-20)
INSERT INTO products (id, name, description, category_id, price) VALUES
(1, 'Wireless Mouse', 'Bluetooth ergonomic mouse', 1, 25.99),
(2, 'Fiction Book', 'Best-selling novel', 2, 12.50),
(3, 'Jeans', 'Denim blue jeans', 3, 39.99),
(4, 'Toaster', '2-slice toaster', 4, 29.99),
(5, 'Face Cream', 'Moisturizing cream', 5, 18.75),
(6, 'Action Figure', 'Superhero toy', 6, 15.00),
(7, 'Car Vacuum', 'Portable vacuum cleaner', 7, 45.00),
(8, 'Desk Chair', 'Ergonomic office chair', 8, 120.00),
(9, 'Yoga Mat', 'Non-slip mat', 9, 20.00),
(10, 'Olive Oil', '500ml bottle', 10, 7.50),
(11, 'Lawn Mower', 'Electric mower', 11, 150.00),
(12, 'Guitar', 'Acoustic guitar', 12, 85.00),
(13, 'Notebook Set', '5-pack A5 notebooks', 13, 9.99),
(14, 'Dog Leash', 'Nylon leash', 14, 11.99),
(15, 'Gold Ring', '18k gold ring', 15, 199.00),
(16, 'Running Shoes', 'Men size 9', 16, 65.00),
(17, 'Baby Wipes', 'Pack of 100', 17, 4.99),
(18, 'Thermometer', 'Digital thermometer', 18, 10.50),
(19, 'Duffel Bag', 'Travel bag', 19, 35.00),
(20, 'Game Controller', 'Wireless controller', 20, 49.99);

-- Inventory
INSERT INTO inventory (product_id, quantity) VALUES
(1, 100), (2, 80), (3, 60), (4, 70), (5, 50),
(6, 90), (7, 40), (8, 30), (9, 120), (10, 200),
(11, 10), (12, 15), (13, 160), (14, 75), (15, 5),
(16, 55), (17, 300), (18, 110), (19, 45), (20, 35);

-- Inventory Logs
INSERT INTO inventory_logs (id, product_id, quantity_change, change_type) VALUES
(1, 1, -10, 'DECREASE'), (2, 2, 20, 'INCREASE'), (3, 3, -5, 'DECREASE'),
(4, 4, 15, 'INCREASE'), (5, 5, -2, 'DECREASE'), (6, 6, -4, 'DECREASE'),
(7, 7, 10, 'INCREASE'), (8, 8, -1, 'DECREASE'), (9, 9, -8, 'DECREASE'),
(10, 10, 25, 'INCREASE'), (11, 11, -3, 'DECREASE'), (12, 12, 5, 'INCREASE'),
(13, 13, -7, 'DECREASE'), (14, 14, 10, 'INCREASE'), (15, 15, -1, 'DECREASE'),
(16, 16, 8, 'INCREASE'), (17, 17, -20, 'DECREASE'), (18, 18, 12, 'INCREASE'),
(19, 19, -6, 'DECREASE'), (20, 20, 5, 'INCREASE');

-- Sales
INSERT INTO sales (id, sale_date, total_amount) VALUES
(1, '2024-01-01 10:00:00', 79.48), (2, '2024-01-02 12:30:00', 25.00), (3, '2024-01-03 14:00:00', 49.99),
(4, '2024-01-04 16:00:00', 129.99), (5, '2024-01-05 18:00:00', 89.99), (6, '2024-01-06 11:00:00', 99.99),
(7, '2024-01-07 13:15:00', 45.50), (8, '2024-01-08 15:45:00', 19.99), (9, '2024-01-09 17:30:00', 75.00),
(10, '2024-01-10 09:45:00', 155.00), (11, '2024-01-11 10:00:00', 49.50), (12, '2024-01-12 12:30:00', 200.00),
(13, '2024-01-13 14:00:00', 60.00), (14, '2024-01-14 16:00:00', 90.00), (15, '2024-01-15 18:00:00', 29.99),
(16, '2024-01-16 11:00:00', 44.99), (17, '2024-01-17 13:15:00', 15.99), (18, '2024-01-18 15:45:00', 300.00),
(19, '2024-01-19 17:30:00', 180.00), (20, '2024-01-20 09:45:00', 90.00);

-- Sale Items
INSERT INTO sale_items (id, sale_id, product_id, quantity, price_per_unit) VALUES
(1, 1, 1, 2, 25.99), (2, 1, 2, 1, 12.50), (3, 2, 3, 1, 25.00),
(4, 3, 20, 1, 49.99), (5, 4, 8, 1, 120.00), (6, 4, 4, 1, 29.99),
(7, 5, 5, 2, 18.75), (8, 6, 7, 2, 45.00), (9, 7, 9, 1, 20.00),
(10, 7, 6, 1, 25.50), (11, 8, 13, 2, 9.99), (12, 9, 16, 1, 65.00),
(13, 10, 11, 1, 150.00), (14, 11, 12, 1, 49.50), (15, 12, 15, 1, 199.00),
(16, 13, 10, 2, 7.50), (17, 14, 14, 3, 11.99), (18, 15, 17, 2, 4.99),
(19, 16, 18, 3, 10.50), (20, 17, 19, 1, 15.99);

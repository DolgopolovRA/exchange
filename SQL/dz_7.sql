mysql> SELECT id, name FROM users WHERE id IN (SELECT DISTINCT user_id FROM orders);

mysql> SELECT id, name, price (SELECT name FROM catalogs WHERE id = products.catalog_id) AS cat_name FROM products;

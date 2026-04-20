USE  northwind;

-- 1) Write a query to list the product id, product name, and unit price of every product.
-- This time, display them in ascending order by price.
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC; 

-- 2) What are the products that we carry where we have at least 100 units on hand? 
-- Sirop d'rable, Grandma's Boysenberry Spread, Pt chinois, Gustaf's Knckebrd, Inlagd Sill,
-- Boston Crab Meat, Rd Kaviar, Sasquatch Ale, Rhnbru Klosterbier, Geitost. 
-- Order them in descending order by price.
SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- 3) What are the products that we carry where we have at least 100 units on hand?
-- Sirop d'rable, Grandma's Boysenberry Spread, Pt chinois, Gustaf's Knckebrd, Inlagd Sill,
-- Boston Crab Meat, Rd Kaviar, Sasquatch Ale, Rhnbru Klosterbier, Geitost.
-- Order them in descending order by price.
-- If two or more have the same price, list those in ascending order by product name.
SELECT ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- 4) Write a query against the orders table that displays the total number of distinct
-- customers who have placed orders, based on customer ID. Use an alias to label the
-- count calculation as CustomerCount.
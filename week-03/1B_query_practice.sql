USE  northwind;

-- 1) Write a query to list the product id, product name, and unit price of every product that Northwind sells.
-- (Hint: To help set up your query, look at the schema preview to see what column names belong to each table.
-- Or use SELECT * to query all columns first, then refine your query to just the columns you want.)
SELECT ProductID, ProductName, UnitPrice
FROM products;

-- 2) Write a query to identify the products where the unit price is $7.50 or less.
-- Tourtire, Filo Mix, Konbu, Guaran Fantstica, Geitost.
SELECT UnitPrice, ProductName
FROM products
WHERE UnitPrice <= 7.50;

-- 3) What are the products that we carry where we have no units on hand, but 1 or more
-- units are on backorder? Write a query that answers this question.
-- Gorgonzola Telino. 
SELECT UnitsInStock, UnitsOnOrder, ProductName
FROM products
WHERE UnitsInStock = 0
	AND UnitsOnOrder > 0;

-- 4) Examine the products table. How does it identify the type (category) of each item sold? Through CategoryID.
-- Where can you find a list of all categories? Write a set of queries to answer these
-- questions, ending with a query that creates a list of all the seafood items we carry.
SELECT * FROM categories;
SELECT * FROM products;
SELECT ProductID, ProductName, CategoryID FROM products;
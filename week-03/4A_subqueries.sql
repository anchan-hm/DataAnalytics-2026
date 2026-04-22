USE northwind;

-- 1) What is the product name(s) of the most expensive products?
-- Cte de Blaye
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice=(SELECT
		MAX(UnitPrice)
        FROM products);

-- 2) What is the product name(s) and categories of the least expensive products?
-- Geitost, Dairy Product.
SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM products AS p
INNER JOIN categories AS c
	ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice=(SELECT
		MIN(UnitPrice)
        FROM products);

-- 3) What is the order id, shipping name and shipping address of all orders shipped via
-- "Federal Shipping"?
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia=
	(SELECT ShipperID
    FROM shippers
    WHERE CompanyName=
    'Federal Shipping');

-- 4) What are the order ids of the orders that included "Sasquatch Ale"
SELECT OrderID
FROM `order details`
WHERE ProductID=
	(SELECT ProductID
    FROM products
    WHERE ProductName=
    'Sasquatch Ale');

-- 5) What is the name of the employee that sold order 10266?
-- Janet Leverling
SELECT e.FirstName, e.LastName
FROM orders AS o
INNER JOIN employees AS e
	ON o.EmployeeID=e.EmployeeID
WHERE o.OrderID=10266;

-- 6) What is the name of the customer that bought order 10266?
-- Pirkko Koskitalo
SELECT c.ContactName
FROM orders AS o
INNER JOIN customers AS c
	ON o.CustomerID=c.CustomerID
WHERE o.OrderID=10266;
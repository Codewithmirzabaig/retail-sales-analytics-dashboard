-- Query 1: Total Sales & Profit
SELECT 
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales;


-- Query 2: Sales by Category
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;


-- Query 3: Top Sub-Categories
SELECT 
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS total_sales
FROM sales
GROUP BY "Sub-Category"
ORDER BY total_sales DESC
LIMIT 10;


-- Query 4: Profit by Region
SELECT 
    Region,
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY Region
ORDER BY total_profit DESC;


-- Query 5: Loss-Making Products
SELECT 
    "Sub-Category",
    ROUND(SUM(Profit), 2) AS total_profit
FROM sales
GROUP BY "Sub-Category"
HAVING total_profit < 0
ORDER BY total_profit;
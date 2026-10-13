--1 What is the total revenue generated?	
SELECT SUM("Revenue") AS total_revenue 
FROM ecommerce;

--2	Which categories generate the highest revenue?	
SELECT "Category", SUM("Revenue") AS revenue
FROM ecommerce
GROUP BY "Category" 
ORDER BY revenue DESC;

--3	Which cities generate the highest revenue?	
SELECT "City", SUM("Revenue") AS revenue
FROM ecommerce
GROUP BY "City" 
ORDER BY revenue DESC;

--4	What is the Average Order Value (AOV)?
SELECT AVG("Revenue") AS average_order_value
FROM ecommerce;

--5	What percentage of orders are Completed, Cancelled and Returned?	
SELECT "Order_Status", COUNT(*) * 100.0 / SUM(COUNT(*)) OVER() AS percentage 
FROM ecommerce
GROUP BY "Order_Status";

--6	Which payment methods are most frequently used and what revenue do they generate?
SELECT "Payment_Mode", COUNT(*) AS orders, SUM("Revenue") AS revenue 
FROM ecommerce
GROUP BY "Payment_Mode" 
ORDER BY orders DESC;

--7	Compare New vs Returning customers by orders and revenue.	
SELECT "Customer_Type", COUNT(*) AS orders, SUM("Revenue") AS revenue 
FROM ecommerce 
GROUP BY "Customer_Type"
ORDER BY revenue DESC;

--8	Rank products based on revenue.	
SELECT "Product", SUM("Revenue") AS revenue, RANK() OVER (ORDER BY SUM("Revenue") DESC) AS rank
FROM ecommerce
GROUP BY "Product";

--9	What is the monthly revenue trend?	
SELECT DATE_TRUNC('month', "Order_Date") AS month, SUM("Revenue") AS revenue 
FROM ecommerce
GROUP BY month 
ORDER BY month;

--10 Find the top 3 products by revenue within each category.
WITH product_revenue AS (SELECT "Category", "Product", SUM("Revenue") AS revenue 
FROM ecommerce_sal GROUP BY "Category", "Product") SELECT "Category", "Product", revenue, RANK() OVER (PARTITION BY "Category" ORDER BY revenue DESC) AS rank FROM product_revenue;
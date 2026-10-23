CREATE DATABASE IF NOT EXISTS apexplanet_task2;

USE apexplanet_task2;
SHOW DATABASES;
USE apexplanet_task2;

SHOW TABLES;

USE apexplanet_task2;

SHOW TABLES;

SELECT COUNT(*) AS total_records
FROM sales_data;

SELECT *
FROM sales_data
LIMIT 10;

/* what is the total sales amount?
USE apexplanet_task2;

SELECT ROUND(SUM(Total_Sales), 2) AS total_sales
FROM sales_data;

/*which is the TOP 5 Product?
SELECT
    Product,
    ROUND(SUM(Total_Sales), 2) AS revenue
FROM sales_data
GROUP BY Product
ORDER BY revenue DESC
LIMIT 5;

/*what is the total sales for each month?
SELECT
    DATE_FORMAT(Order_Date, '%Y-%m') AS sales_month,
    ROUND(SUM(Total_Sales), 2) AS monthly_sales
FROM sales_data
WHERE Order_Date IS NOT NULL
GROUP BY DATE_FORMAT(Order_Date, '%Y-%m')
ORDER BY sales_month;

/*which category has the highest sales?
SELECT
    Category,
    ROUND(SUM(Total_Sales), 2) AS category_sales
FROM sales_data
GROUP BY Category
ORDER BY category_sales DESC;

/*which city generated the highest sales?
SELECT
    City,
    ROUND(SUM(Total_Sales), 2) AS city_sales
FROM sales_data
WHERE City IS NOT NULL
GROUP BY City
ORDER BY city_sales DESC;

/*compare sales by gender
SELECT
    Gender,
    COUNT(*) AS record_count,
    ROUND(SUM(Total_Sales), 2) AS total_sales
FROM sales_data
GROUP BY Gender
ORDER BY total_sales DESC;

/*Records with sales greater than or equal to the average
SELECT
    Order_ID,
    Order_Date,
    Product,
    Category,
    Quantity,
    Total_Sales
FROM sales_data
WHERE Total_Sales >= (
    SELECT AVG(Total_Sales)
    FROM sales_data
)
ORDER BY Total_Sales DESC;


ALTER TABLE sales_data RENAME COLUMN `ï»¿Order_ID` TO Order_ID;





# Olist-Project Devevelopment Diary


In this file, I include a complete list of all developments made to this project. 

**Please note that the dates below may not be completely in sync with commit history, as this project was performed in the past, and then, later uploaded to Github, which required testing, cleanup, and documentation. These dates, however, are the estimated dates when developments were made.**

0.1: Created 'SQL_Queries.py' to house many of the SQL queries I am using throughout this project. 

0.11: Added data questions added to 'SQL_Queries.py', which were a few questions I wanted to find answers to using SQL.


1. Retrieve all columns for a specific order using its `order_id`
2. List the unique product IDs present in the dataset.
3. Calculate the average price and freight value for all orders.
4. Find the total number of distinct sellers in the dataset.
5. Get the highest and lowest prices among all products
6. Count the number of orders for each unique `product_id`
7. Find the orders with the highest total price (price + freight value).
8. Calculate the average price for each seller.
9. List the orders with a shipping limit date beyond a specific date.
10. Retrieve the total revenue generated from all orders.
    


0.12: Created a stored procedure that will create a new flat table that joins together olist_orders, olist_order_items,  olist_order_payments into one table. This will be considered an analytical table that will be queried often


0.13: Developed a DBT connection to BigQuery / GCP. Configured the new model so it will be materialized as a table, and a second model as a view. 

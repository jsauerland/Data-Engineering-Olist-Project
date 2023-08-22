# Olist-Project Devevelopment Diary


In this file, I include a complete list of all developments made to this project. 

**Please note that the dates below may not be completely in sync with commit history, as this project was performed in the past, and then, later uploaded to Github, which required testing, cleanup, and documentation. These dates, however, are the estimated dates when developments were made.**

8/2/2023: Created 'SQL_Queries.py'

8/5/2023: Added data questions added to 'SQL_Queries.py':


1. Retrieve all columns for a specific order using its `order_id`
2. List the unique product IDs present in the dataset
3. Calculate the average price and freight value for all orders.
4. Find the total number of distinct sellers in the dataset.
5. Get the highest and lowest prices among all products
6. Count the number of orders for each unique `product_id`
7. Find the orders with the highest total price (price + freight value).
8. Calculate the average price for each seller.
9. List the orders with a shipping limit date beyond a specific date.
10. Retrieve the total revenue generated from all orders.
    

Remember, these questions can serve as starting points for your SQL practice with the 'olist_order_items_dataset'. You can gradually increase the complexity of your queries as you become more comfortable with SQL.

8/22/23: Created a stored procedure that will create a new flat table that joins together olist_orders, olist_order_items,  olist_order_payments into one table. This will be considered an analytical table that will be queried often
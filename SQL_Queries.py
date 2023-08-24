#Import libraries needed
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from google.oauth2 import service_account
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import pandas as pd



# Set Google Application Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'BQ_KEY.json' # BigQuery Key
key_path = 'BQ-olist-ecommerce-key.json'

# Create a BigQuery client instance (bigquery_client)

credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project='olist-ecommerce-project') 
project_id = 'olist-ecommerce-project'  

# ???

sql_query_1 = """ 
WITH OrderSummary AS (
    SELECT 
        order_status, 
        COUNT(DISTINCT order_id) AS `Order Count`,
        ROUND(COUNT(DISTINCT order_id) / SUM(COUNT(DISTINCT order_id)) OVER () * 100, 2) AS `Percent of Total`
    FROM  
        `olist-ecommerce-project.ecommerce_data.olist_orders_dataset` 
    GROUP BY 
        order_status
)
SELECT 
    order_status, 
    `Order Count`,
    `Percent of Total`
FROM 
    OrderSummary
ORDER BY 
    `Order Count` DESC;

"""

# retrieve customers who have not placed an order.

sql_query_2 = """ 
WITH CustomersWithoutOrders AS (
  SELECT a.customer_id
  FROM `ecommerce_data.olist_customers_dataset` AS a
  WHERE NOT EXISTS (
    SELECT 1
    FROM `ecommerce_data.olist_orders_dataset` AS b
    WHERE a.customer_id = b.customer_id
  )
)

SELECT customer_id
FROM CustomersWithoutOrders;

"""

# Retrieve total revenue for all orders

sql_query_3 = """ 
SELECT SUM(A.price) AS total_revenue, product_id
FROM `ecommerce_data.olist_order_items_dataset` AS A
LEFT OUTER JOIN `ecommerce_data.olist_orders_dataset` AS B ON A.order_id = B.order_id
GROUP BY product_id
ORDER BY total_revenue desc
"""

# Find the orders with the highest total price (price + freight value).

sql_query_4 = """
WITH TotalPriceCTE AS ( 
  SELECT A.order_id, A.product_id, C.product_category_name_english, ROUND(SUM (price + freight_value),2) AS TotalPrice
  
  FROM `ecommerce_data.olist_order_items_dataset` as A
  LEFT JOIN `ecommerce_data.olist_products_dataset` as B on A.product_id = B.product_id
  LEFT JOIN `ecommerce_data.product_category_name_translation` as C on B.product_category_name = C.product_category_name

  GROUP BY A.order_id, A.product_id, C.product_category_name_english

)
 
SELECT product_category_name_english, TotalPrice from TotalPriceCTE
ORDER BY TotalPrice DESC
"""

# 9. List the orders with a shipping limit date beyond a specific date.

sql_query_5 = """
SELECT 
    A."order_id", 
    COALESCE(A."customer_id", B."customer_id") AS "customer_id", 
    A."order_status", 
    A."order_purchase_timestamp", 
    A."order_approved_at", 
    A."order_delivered_carrier_date", 
    A."order_delivered_customer_date", 
    A."order_estimated_delivery_date"
FROM ecommerce_data.olist_orders_dataset A
LEFT JOIN ecommerce_data.olist_customers_dataset B ON A."customer_id" IS NULL AND A."customer_id" = B."customer_id"
WHERE A."order_purchase_timestamp" > '2017-05

"""

df = pd.read_gbq(sql_query_1, project_id = project_id, credentials=credentials, dialect = 'standard')

print(df.head)
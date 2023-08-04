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

# API request - fetch the table

sql_query = """ 
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

df = pd.read_gbq(sql_query, project_id = project_id, credentials=credentials, dialect = 'standard')

print(df.head)
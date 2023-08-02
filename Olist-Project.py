import kaggle
import pandas as pd
import pandas_gbq
import os
from google.cloud import bigquery
api = kaggle.api
datasets = kaggle.api.dataset_list(search="covid")

# kaggle.api.dataset_download_files('olistbr/brazilian-ecommerce',  unzip=True) # This is commented out after it is run because re-running it will re-pull the data from Kaggle using bandwith and CPU resources unnecessarily


csv_files = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
]


dataframes = {}     # Create an empty dictionary to store dataframes


for idx, csv_file in enumerate(csv_files):      # Loop through the list of filenames and read CSV files into dataframes
    df_name = f"df_{idx + 1}"                   # Generate dataframe variable name
    dataframes[df_name] = pd.read_csv(csv_file)

print(list(dataframes.keys()))
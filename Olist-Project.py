#Import libraries needed
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from google.oauth2 import service_account
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import pandas as pd
import pandas_gbq
import zipfile

# Configure Kaggle API
api = kaggle.api

# Set Google Application Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'BQ_KEY.json' # this is your account details JSON file
key_path = 'BQ-olist-ecommerce-key.json'

# Create a BigQuery client instance (bigquery_client)


credentials = service_account.Credentials.from_service_account_file(
    key_path
)

client = bigquery.Client(credentials=credentials, project='olist-ecommerce-project') # Create a BigQuery client instance (bigquery_client)

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


# Define the Google Cloud project ID
project_id = 'olist-ecommerce-project'  # Replace with your actual project ID

# Assuming df_1 is the DataFrame you want to import into BigQuery
df_1 = dataframes['df_1']


# Import df_1 into BigQuery


export_df = pandas_gbq.to_gbq(
    df_1, 
    'ecommerce_data.test_table_1', 
    project_id='olist-ecommerce-project', 
    if_exists='replace',
)

if __name__ == "__main__": # Loop through the dataframes and export each to BigQuery
    for df_name, df in dataframes.items():
        table_name = f'ecommerce_data.{df_name}'  # Define the BigQuery table name
        pandas_gbq.to_gbq(
            df,
            table_name,
            project_id=project_id,
            if_exists='replace',
        )

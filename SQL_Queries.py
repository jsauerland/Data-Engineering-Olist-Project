#Import libraries needed
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from google.oauth2 import service_account
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import os
import pandas as pd
import pandas_gbq
import tqdm as tq

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
    df_name = csv_file.replace('.csv', '')     # Remove the '.csv' extension from the filename
    dataframes[f"df_{idx + 1}"] = pd.read_csv(csv_file)

order_items_columns = dataframes['df_3'].columns
print(f"Columns in DataFrame {'df_3'}:", order_items_columns)



# Define the Google Cloud project ID
project_id = 'olist-ecommerce-project'  # Replace with your actual project ID


# if __name__ == "__main__":
#     # Loop through the dataframes and export each to BigQuery
#     for df_name, df in tq.tqdm(dataframes.items(), desc='Exporting to BigQuery', unit='table'):
#         table_name = f'ecommerce_data.{df_name}'
#         pandas_gbq.to_gbq(
#             df,
#             table_name,
#             project_id=project_id,
#             if_exists='replace',
#         )
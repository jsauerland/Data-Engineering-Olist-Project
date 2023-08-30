# Data-Engineering-Olist-Project 



In order to practice and enhance my data engineeering skillset, I launched a project to model data, create data pipelines, a data lake, and much more. This helped me to further my understanding of Data Engineering both practically and conceptually. For this project, I am using Azure to setup a Data Lake. 

### Project Goals

- Broaden my knowledge of big data infrastructure, data warehousing
- Develop cloud-based data warehouses on modern Cloud Data Warehouse applications: Google BigQuery, Apache Cassandra, Spark, Amazon Redshift, etc.
- Deepen my understanding of big data ecosystems
- Learn how Data Pipelines work in detail


# Part 1: Establishing the Data Warehouses

For this project, I used several completely different applications and cloud data warehouses in order to gain more exposure, and understanding of different CDWs, and how they differ in form and function. These include Apache Cassandra, Snowflake, Azure Data Lake, Google BigQuery, and SQL SERVER.

##### Data Build Tool (DBT)

In DBT, you can change things between tables and views by changing a keyword rather than writing the data definition language (DDL) to do this behind the scenes

The tool acts as an extra layer on top of your data warehouse to improve data transformation and integration, which in turn, makes things much easier. It also allows you to neatly organize all transformations into discrete models. This takes out the guesswork in running DDL, and trying to "take a stab in the dark" instead of just deploying a well functioning data model. 

# Part 2: Extracting and Loading the data

In this stage, I wrote an API to retrieve data from Kaggle, and another API to interface with a new project in Google BigQuery. Then, I retrieved and extracted all of the files from Kaggle, and using enumeration, looped through all of the files to create Pandas Dataframes. Finally, after creating the dataframes, I piped the data directly into Google BigQuery using the API into brand new tables.  

# Part 3: Modeling the data (ELT)


In all of the applications I used, I first loaded the extracts into the Data Warehouse, and then transformation takes place in the target system. The data was not transformed on submission to the data warehouse, but stored in its original format.

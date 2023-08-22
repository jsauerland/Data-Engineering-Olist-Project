---- Creating tables in SQL Server ----

-- Create olist_customers table
CREATE TABLE olist_customers (
    customer_id INT PRIMARY KEY,
    customer_unique_id VARCHAR(255),
    customer_zip_code_prefix VARCHAR(10),
    customer_city VARCHAR(255),
    customer_state VARCHAR(255)
);

-- Create olist_geolocation table
CREATE TABLE olist_geolocation (
    geolocation_zip_code_prefix VARCHAR(10) PRIMARY KEY,
    geolocation_lat FLOAT,
    geolocation_lng FLOAT,
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(255)
);

-- Create olist_order_items table
CREATE TABLE olist_order_items (
    order_id VARCHAR(50) PRIMARY KEY,
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATETIME,
    price DECIMAL(18, 2),
    freight_value DECIMAL(18, 2)
);

-- Create olist_order_payments table
CREATE TABLE olist_order_payments (
    order_id VARCHAR(50) PRIMARY KEY,
    payment_sequential INT,
    payment_type VARCHAR(50),
    payment_installments INT,
    payment_value DECIMAL(18, 2)
);

-- Create olist_order_reviews table
CREATE TABLE olist_order_reviews (
    review_id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50),
    review_score INT,
    review_comment_title VARCHAR(255),
    review_comment_message TEXT,
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME
);

-- Create olist_orders table
CREATE TABLE olist_orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id INT,
    order_status VARCHAR(50),
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME
);

-- Create olist_products table
CREATE TABLE olist_products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- Create olist_sellers table
CREATE TABLE olist_sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(10),
    seller_city VARCHAR(255),
    seller_state VARCHAR(255)
);

-- Create product_category_name_translation table
CREATE TABLE product_category_name_translation (
    product_category_name VARCHAR(255) PRIMARY KEY,
    product_category_name_english VARCHAR(255)
);

---- Stored procedure to create an analytical table for users to query

CREATE PROCEDURE CreateAnalyticalTable AS
BEGIN
    -- Drop the analytical table if it already exists
    IF OBJECT_ID('analytical_table') IS NOT NULL
        DROP TABLE analytical_table;

    -- Create the analytical table by joining the required tables
    SELECT
        A.order_id,
        A.customer_id,
        A.order_status,
        A.order_purchase_timestamp,
        A.order_approved_at,
        A.order_delivered_carrier_date,
        A.order_delivered_customer_date,
        A.order_estimated_delivery_date,
        B.order_item_id,
        B.product_id,
        B.seller_id,
        B.shipping_limit_date,
        B.price,
        B.freight_value,
        C.payment_sequential,
        C.payment_type,
        C.payment_installments,
        C.payment_value
    INTO analytical_table
    FROM olist_orders AS A
    JOIN olist_order_items AS B ON A.order_id = B.order_id
    JOIN olist_order_payments AS C ON A.order_id = C.order_id;

    -- Create any necessary indexes or constraints on the analytical_table if needed
    -- CREATE INDEX idx_analytical_table_customer_id ON analytical_table(customer_id);
    -- ...

    PRINT 'Analytical table created successfully.';
END;



---- Creating tables in Google BigQuery ----
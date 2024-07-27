# E-Commerce-DataPipeline
***
## Project Overview
This project is an overview of an e-commerce data pipeline that involves building a sophisticated event-driven data ingestion and transformation pipeline focusing on e-commerce transactional data.
We will design a system using AWS services such as S3, Lambda, Glue, Redshift, and SNS to ingest, transform, validate, and upsert data into Amazon Redshift for analytical purposes.
***


## Architectural Diagram
![Architecture Design](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/Dim_Customer.JPG)

***

## Key Steps
### 1. Dimension Tables and Sample Records
- Products Dimension Table (dim_products):
    - Columns: product_id, product_name, category, price, supplier_id
      ![Dim_Customer](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/Dim_Product.JPG)
      
- Customers Dimension Table (dim_customers):
    - Columns: customer_id, first_name, last_name, email, membership_level
      ![Dim_Customer](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/Dim_Customer.JPG)
      
- Pre-load these dimension tables into Redshift as part of the setup process.

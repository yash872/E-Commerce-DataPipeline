# E-Commerce-DataPipeline
***
## Project Overview
This project is an overview of an e-commerce data pipeline that involves building a sophisticated event-driven data ingestion and transformation pipeline focusing on e-commerce transactional data.
We will design a system using AWS services such as S3, Lambda, Glue, Redshift, and SNS to ingest, transform, validate, and upsert data into Amazon Redshift for analytical purposes.
***


## Architectural Diagram
![Architecture Design](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/E-CommerceDataPipeline.png)

***

## Key Steps
### 1. Dimension Tables with Sample Records and Fact Table 
- Pre-load these dimension tables into Redshift as part of the setup process.
- Products Dimension Table (dim_products):
    - Columns: product_id, product_name, category, price, supplier_id
      ![Dim_Customer](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/Dim_Product.JPG)
      
- Customers Dimension Table (dim_customers):
    - Columns: customer_id, first_name, last_name, email, membership_level
      ![Dim_Customer](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/Dim_Customer.JPG)

- Transactions Fact Table (fact_transactions):
    - Columns: transaction_id, customer_id, customer_email, product_id, product_name, total_price, transaction_date, payment_type, status   


***

### 2. Mock Data Generation
- Generate Mock Data for the customers based on products. Use Code build for lambda. This lambda function will generate data and upload csv files into S3 in Hive
Partitioning manner.
  - CODE BUILD:
  ![Codebuild](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/codebuild.JPG)
  
  - Mock CSV files generated from the Lambda, the code in lambda is updated from GitHub repo by the CICD setup with AWS CodeBuild.
  stored using the following hive-style partitioning in S3: 
  s3://your-bucket/transactions/year=2023/month=03/day=15/transactions_2023-03-15.csv.

   ![RawCSVFiles](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/RawCSVFiles.JPG)
  
  ***

### 3. Create AWS Glue Crawlers
- Create a Glue crawler for the S3 bucket input file directory (data stored in HIVE style with multiple partitioning)
- Create a Glue crawler for the fact_transaction Redshift table.
  NOTE: we have to create the Redshift connector and 2 important points to remember
  - Security Group associated with Redshift should be exposed to the Redshift PORT 5439.
  - VPC associated with Redshift should have a S3 Endpoint defined.

![crawlers](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/crawlers.JPG)

  ***

### 4. Create Glue ETL Flow
- ![GlueETL](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/GlueETLJob.JPG)


### 5. Create lambda to start the glue job when data is generated in S3:
- ![s3lambdaGlueJob](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/s3lambdaGlueJob.JPG)

### 6. Create SNS Topic:
- Create an SNS Topic to send emails when Glue ETL job is done, and it can be used in the final 
lambda to archive the data
  - ![s3lambdaGlueJob](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/GlueJobNotification.JPG)

### 7. Create EventBridge Rule:
- Create EventBridge Rule to trigger SNS when Glue Job Changes Status
  - ![EventRuleforSNS](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/EventRuleforSNS.JPG)

### 8. Create lambda to archive data after SNS notification:
- ![s3lambdaGlueJob](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/s3lambdaGlueJob.JPG)

### 9. Create S3 Bucket to Archive the data:
- ![dataArchive](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/dataArchive.JPG)

### 10. Final Fact_Transaction table in Redshift:
- The data ingestion process is following the UPSERT method.
  - ![fact_ouput](https://github.com/yash872/E-Commerce-DataPipeline/blob/main/Images/fact_ouput.JPG)

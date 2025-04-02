# Global Product Inventory Analysis

## Introduction
This Global Product Inventory Analysis project is an innovative end-to-end Data Engineering (DE) pipeline designed to streamline data handling and visualization. The workflow begins by sourcing data from Kaggle, followed by storing it securely in Google Cloud Storage. The data is then meticulously transformed to ensure accuracy and completeness before being loaded into BigQuery for efficient querying and analysis. To bring insights to life, the project leverages Looker Studio for creating visually compelling dashboards. With its well-orchestrated architecture, this project exemplifies the essence of modern data engineering by seamlessly integrating data ingestion, transformation, storage, and visualization into a unified solution.

## Project Description
### Project Goal
The goal of this project is to provide actionable recommendations for improving product storage and optimizing supply chain operations.
### Dataset Description
This dataset provides a comprehensive overview of global product inventory, making it an invaluable resource for optimizing logistics, analyzing e-commerce trends, or conducting supply chain research. It features 14 detailed columns, including unique identifiers such as Product ID and descriptive attributes like Product Name, Category, and Description. Key metrics such as Price, Stock Quantity, and Warrantly Period are included, alongside logistical details like Product Dimensions, Manufacturing Date, and Expiration Date. The dataset also tracks inventory using SKU codes, highlights customer preferences with Product Rating, and offers insights into Color/Size Variations and Product Tags. [Dataset](https://www.kaggle.com/datasets/keyushnisar/global-product-inventory-dataset-2025/data)
### Tools
* **Mage**:workflow orchestration for ingesting data, transforming, and exporting to data lake
* **Docker**: containerizing mage
* **Google Cloud Storage**: storage data
* **Colab**:generate python script for Spark
* **Spark**：transform and partition the dataset
* **Google Bigquery**: performi SQL analytical queries and storage structured data
* **Google Looker Studio**: create a dashaborad for visualization
### Data Pipeline 
* Mage Pipeline:
  
  api to gsc
  
  <img src="image//api_to_gcs.png" alt="api_to_gcs" width="250" />

  



!gcloud dataproc jobs submit pyspark \
    --cluster=cluster-7c18 \
    --region=us-east1 \
    gs://global_inventory_data/clean_data_code_bigquery.py \
    --\
        --input_data=gs://global_inventory_data/clean_data/raw/ \
        --output_report=global_inventory.report-2025 \  #output transformed data to Bigquery
        --output_data=global_inventory.cleandata  #output cleaned data Bigquery

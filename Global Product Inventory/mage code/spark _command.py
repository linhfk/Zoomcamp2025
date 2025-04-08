gcloud dataproc jobs submit pyspark \
    --cluster=cluster-7c18 \
    --region=us-east1 \
    gs://global_inventory_data/clean_data_code.py \
    --\
        --input_data=gs://global_inventory_data/clean_data/raw/ \
        --output_report=gs://global_inventory_data/clean_data/spark_submit/report \  #load transformed data to biquery
        --output_data=gs://global_inventory_data/clean_data/spark_submit/pq  #load raw data to biquery

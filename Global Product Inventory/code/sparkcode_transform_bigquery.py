
import argparse
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
import pandas as pd

parser = argparse.ArgumentParser()

parser.add_argument('--input_data', required=True)
parser.add_argument('--output_report', required=True)
parser.add_argument('--output_data', required=True)

args = parser.parse_args()

input_data = args.input_data
output_report = args.output_report
output_data = args.output_data

spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket', 'dataproc-temp-us-east1-891469561669-rrcqgwps')

df_Inv = spark.read.parquet(input_data)

df = df_Inv.toPandas()                                                          #Convert Spark to Pandas Dataframe

df.columns = [col.replace("/", "_").replace(" ", "_") for col in df.columns]    # replace '/' and ' ' to '_'

df['Shelf_Life'] = (df['Expiration_Date']-df['Manufacturing_Date']).dt.days     # add Shelf_Life column

df['Dimensions']=df['Product_Dimensions'].str.replace(' cm', '')                # Split the Dimension to Length, width, and Height, and add Volume column
dim = df['Dimensions'].str.split('x', expand=True)
df['Length'] = dim[0].astype(float)
df['Width'] = dim[1].astype(float)
df['Height'] = dim[2].astype(float)
df['Volume'] = df['Length'] * df['Width'] * df['Height']
df.drop(columns=['Dimensions'], inplace=True)

df_spark = spark.createDataFrame(df)

df_spark.registerTempTable("inventory")

df_result = spark.sql("""
SELECT
    --
    Product_Category,
    Product_Name,
    date_format(Manufacturing_Date, 'yyyy-MM') AS Manufacturing_Month,  -- Formatted to year-month


    --
    SUM(Stock_Quantity) AS total_stock_quantity,
    avg(Stock_Quantity) AS avg_stock_quantity,
    avg(Warranty_Period) AS avg_warranty_period,
    avg(Product_Ratings) as avg_product_ratings,
    avg(Shelf_Life) AS avg_shelf_life,
    SUM(Volume) AS total_volume,
    avg(Volume) AS avg_volume,
    sum(Stock_Quantity*Price) AS total_cost


FROM
    inventory
GROUP BY
    Product_Category,
    Product_Name,
    Manufacturing_Month

order by
    Product_Category,
    Product_Name

""")



df_result.coalesce(1).write.format('bigquery') \              # saved the transformed data to bigquery
    .option('table', output_report) \
    .mode('overwrite') \
    .save()

df_spark.write.format('bigquery') \                           # save the clean data to bigqyery
    .option('table', output_data) \
    .mode('overwrite') \
    .save()


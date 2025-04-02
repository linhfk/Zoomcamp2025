import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://www.kaggle.com/api/v1/datasets/download/keyushnisar/global-product-inventory-dataset-2025'
    
    datatypes={
                    'Product ID': str, 
                    'Product Name':str,
                    'Product Category':str,
                    'Product Description':str,
                    'Price':float,
                    'Stock Quantity':int,
                    'Warranty Period':int,
                    'Product Dimensions':str,
                    'SKU':str,
                    'Product Tags':str,
                    'Color/Size Variations':str,
                    'Product Ratings':float,

    }

    parse_dates = ['Manufacturing Date','Expiration Date']
    return pd.read_csv(url,sep=",",compression='zip',dtype=datatypes, parse_dates=parse_dates)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'



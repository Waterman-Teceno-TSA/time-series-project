from re import S


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from env import user, host, password

def get_db_url(db_name, username=user, hostname=host, password=password):
    '''
    This function requires a database name (db_name) and uses the imported username,
    hostname, and password from an env file.
    A url string is returned using the format required to connect to a SQL server.
    '''
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return url


query = '''
SELECT  orders.*,
        categories.`Category`, categories.`Sub-Category`,
        customers.`Customer Name`,
        products.`Product Name`,
        regions.`Region Name`        

FROM orders
LEFT JOIN categories USING (`Category ID`)
LEFT JOIN customers USING (`Customer ID`)
LEFT JOIN products USING (`Product ID`)
LEFT JOIN regions USING (`Region ID`)
'''

def acquire_superstore(use_cache = False):
    '''
    
    '''
    if os.path.exists('superstore.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('superstore.csv')
    
    superstore_df = pd.read_sql(query, get_db_url('superstore_db'))

    superstore_df.to_csv('superstore.csv', index=False)
    # rename all columns to lowercase
    superstore_df.columns = [c.lower() for c in superstore_df.columns]
    # replace spaces in column names with underscores
    superstore_df.columns = [c.replace(' ', '_') for c in superstore_df.columns]
    # replace - with _ in column names
    superstore_df.columns = [c.replace('-', '_') for c in superstore_df.columns]
    # convert the date columns to datetime
    superstore_df['order_date'] = pd.to_datetime(superstore_df['order_date'])
    superstore_df['ship_date'] = pd.to_datetime(superstore_df['ship_date'])
    
    return superstore_df
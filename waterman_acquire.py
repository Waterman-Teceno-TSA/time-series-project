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

def acquire_superstore(use_cache = True):
    '''
    
    '''
    if os.path.exists('superstore.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('superstore.csv')
    
    superstore_df = pd.read_sql(query, get_db_url('superstore_db'))

    superstore_df.to_csv('superstore.csv', index=False)

    return superstore_df
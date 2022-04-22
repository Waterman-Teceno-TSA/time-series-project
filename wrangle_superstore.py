# Import OS
import os

# Import pandas and numpy for dataframe manipulations
import pandas as pd
import numpy as np

# Import credentials for SQL pull
from env import user, host, password

# --- SQL Interaction url
def get_db_url(db_name, username=user, hostname=host, password=password):
    """
    This function requires a database name (db_name) and uses the imported username,
    hostname, and password from an env file.
    A url string is returned using the format required to connect to a SQL server.
    """
    url = f"mysql+pymysql://{username}:{password}@{host}/{db_name}"
    return url


# Query for SQL pull
query = """
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
"""

# Acquire function
def acquire_superstore(use_cache=True):
    """
    This function acquires the superstore_db data and creates a dataframe out of it. This dataframe has some basic manipulations performed prior to returning.
    Unnecessary columns are dropped, the date columns are properly converted to datatime format, and postal code is properly converted to an object type. 
    """
    # Checking if there is a local .csv file already in cache
    if os.path.exists("superstore.csv") and use_cache:
        print("Using cached csv")
        df = pd.read_csv("superstore.csv")
        return df
    # SQL query using credentials and query
    df = pd.read_sql(query, get_db_url("superstore_db"))
    # Creation of .csv file
    df.to_csv("superstore.csv", index=False)
    # Return the dataframe
    return df


def prepare_superstore(df):
    """
    This function takes our dataframe and feature engineers a unit_cost, unit_profit, and brand column. It then rounds the sales and profit columns. 
    """
    # rename all columns to lowercase
    df.columns = [c.lower() for c in df.columns]
    # replace spaces in column names with underscores
    df.columns = [c.replace(" ", "_") for c in df.columns]
    # replace - with _ in column names
    df.columns = [c.replace("-", "_") for c in df.columns]
    # Dropping duplicate columns
    df = df.drop(
        columns=["customer_name", "region_id", "category_id", "country", "product_id"]
    )
    # Converting order_date to datetime format
    df["order_date"] = pd.to_datetime(df["order_date"])
    # Converting ship_date to datetime format
    df["ship_date"] = pd.to_datetime(df["ship_date"])
    # Changing datatype of postal_code to int (to drop the 0) and then object type
    df.postal_code = df.postal_code.astype(int)
    df.postal_code = df.postal_code.astype(object)
    # Set index to order_date
    df.index = df.order_date
    # Sorting the index
    df = df.sort_index()
    # Creation of unit_cost column
    df["unit_cost"] = df.sales / ((1 - df.discount) * df.quantity)
    # Creation of unit_profit column
    df["unit_profit"] = df.profit / df.quantity
    # Creation of brand column
    df["brand"] = df.product_name.str.split().str[0]
    # Creation of product_line column
    df["product_line"] = df.brand + "_" + df.sub_category
    # Rounding sales and profit to 2 decimal places
    df["sales"] = df.sales.round(2)
    df["profit"] = df.profit.round(2)
    # Return the dataframe
    return df


def wrangle_superstore(use_cache=True):
    """
    This function does both our acquire and prepare functions and returns the dataframe.
    """
    # Acquiring the dataframe from SQL
    df = acquire_superstore(use_cache=use_cache)
    # Additional preparation on the dataframe
    df = prepare_superstore(df)
    # Returning the dataframe
    return df

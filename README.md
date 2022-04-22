# Teceno-Waterman, Superstore_DB Time Series

## Table of Contents
- [Project Goal](#project-goal)
- [Project Description](#project-description)
- [How to Reproduce](#how-to-reproduce)
- [Initial Questions](#initial-questions)
- [Data Dictionary](#data-dictionary)
- [Project Plan](#project-plan)
   - [Wrangling](#wrangling)
      - [Acquire](#acquire)
      - [Preparation and Splitting](#preparation-and-splitting)
  - [Exploration](#exploration)
  - [Clustering](#clustering)
  - [Modeling](#modeling)
  - [Deliverables](#deliverables)
    - [Final Report](#final-report)
    - [Modules](#modules)
    - [Predictions](#predictions)
- [Summary and Recommendations](#summary-and-recommendations)

## Project Goal
The goal of this project is to provide insights about the superstore_db dataset. (Acquired from CodeUp's SQL server) More specifically, to answer: "Which product line should we expand?" for the VP of Product, and expand on any questions that arise from this line of exploration. This will include an overview of such details as profitability, sales volume, and product category. 

## Project Description
Through the analysis of profit and volume metrics the company can better allocate their resources and conclude which product categories or brands are most worth expanding. This can increase the company profits and provide opportunities down the road as the company increases their supply of profitable products and trims the most unnecessary loss leading products. With an emphasis on both category and brand the company can address how to increase profits from both angles simultaneously. 

## How to Reproduce 
To reproduce the outcomes in this project:
1. Have an env.py file with credentials (hostname, username, password) to access a SQL database that contains superstore data. Codeup's 'superstore_db' data was utilized
   for this project. 
2. Clone this repo and ensure you have all of the necessary modules and notebooks. Confirm that the .gitignore includes your env.py file to secure credentials.
3. Use of these libraries: pandas, numpy, matplotlib, seaborn, sklearn.
4. Be able to run the 'Final Report' jupyter notebook file. 
   - Supplemental workbooks may also be useful in identifying some of the steps taken prior to the cleaner final code 

## Initial Questions 
_Initial Data Centric Questions_
From VP of Product:
1. Which product line should we expand?
2. What categories of product are profitable?
3. What details can we tell about these product lines?
    - Sales volume?
    - Customer demographic? 

## Data Dictionary
| Attribute                          | Definition                                         | Data Type | Additional Info                                   |
|:-----------------------------------|:---------------------------------------------------|:---------:|:--------------------------------------------------|
| order_id                           | Unique order ID for each customer                  | object    | Non-unique by product                             |
| order_date                         | Order date of product                              | datetime  | Index of dataframe                                |
| ship_date                          | Shipping date of product                           | datetime  |                                                   |
| ship_mode                          | Shipping mode specified by customer                | object    | Standard, Second, First, Same Day                 |
| customer_id                        | Unique ID to identify customers                    | object    | Non-unique by customer                            |
| segment                            | Segment description for customer                   | object    | Consumer, Corporate, Home Office                  |
| city                               | City of residence of the customer                  | object    |                                                   |
| state                              | State of residence of the customer                 | object    |                                                   |
| postal_code                        | Postal code of customer                            | object    |                                                   |
| sales                              | Sales price of product                             | float     | Sale value after discount                         |
| quantity                           | Quantity of the product                            | float     |                                                   |
| discount                           | Discount applied to product                        | float     | % of discount applied (0.XX)                      |
| profit                             | Profit or loss from product sale                   | float     | Target Variable                                   |
| category                           | Category of the product ordered                    | object    | Office Supplies, Furtniture, Technology           |
| sub_category                       | Sub-category of the product ordered                | object    | 17 more specific descriptions of category         |
| product_name                       | Name/description of the product                    | object    | Description of product to include brand           |
| region_name                        | Region where the customer resides                  | object    | East, West, Central, South                        |
| unit_cost                          | Sales price per unit of product                    | float     | Cost per unit to company                          |
| unit_profit                        | Profit or loss per unit of product                 | float     | Profit or loss per unit (after discount)          |
| brand                              | Brand of product                                   | object    | Brand specified from product_name                 |
| product_line                       | Brand and sub-category of product                  | object    | Specific product_line from brand and sub_category |

## Project Plan
This project will start with some initial planning and question exploration before we even access the data. The question exploration has been delved out in the _Initial Questions_ section. 
Additionally let us detail what is to be provided at the conclusion of this project:
 - This README.md
 - Final Report.ipynb 
 - Workbooks and modules used

### Wrangling 
This section contains our acquisition and preparation of the data.
#### Acquire 
The wrangle_superstore.py file contains the code that was used for acquiring the data. There is a **get_db_url()** function that is used to format the credentials for interacting with a SQL server, and the **acquire_superstore()** function that queries the SQL server for the data. For this project Codeup's 'superstore_db' SQL database was used. The env.py file used, and the credentials within, are not included in this project and as covered under _How To Reproduce_ must be curated with one's own information.

#### Preparation
The wrangle_superstore.py file contains the code that was used for preparing the data. The **prepare_superstore()** function takes the acquired dataframe and cleans it for our exploratory purposes. The primary objectives for this preparation was:
- The engineering of features such as unit_cost, unit_profit, and product_line. 
- Conversion of time data to proper format and setting the order_date to the index of the dataframe
- Proper datatyping of columns and dropping of unnecessary columns

### Exploration
For exploration the data was analyzed by both Waterman and Teceno. A number of univariate, bivariate, and multivariate analysis was conducted to figure out which sub-category had the most potential for product expansion for the company. Additionally, time series analysis was utilized to try and demonstrate which sub-category had the most potential for profit, or expansion, across time with a positive trend. From the exploration the category that provides the most opportunity for the company to expand is Accessories, with an emphasis on computer and gaming accessories. The brands that demonstrated the most opportunity for the company to expand with were Logitech, Plantronic, and Razer in the accessories industry. 

### Deliverables 
The main deliverable from this project are the Final Report. Additionally there are modules that contain the functions used and workbooks where a deeper exploration of the process can be seen.

#### Final Report
The Final Report can be ran to reproduce the same results from start to finish. 

#### Modules
The modules included in this project are:
- wrangle_superstore.py
- viz.py

### Summary and Recommendations
In conclusion the category of product that the company should expand with would be Accessories. Furthermore, from accessories the company should emphasize computer and gaming accessories with the brand Logitech primarily and Plantronic and Razer secondarily. These companies demonstrated a high profit yield for the comapny with stable sales volumes across time. 

Our recommendations for the comapny would be to try and obtain more data about the products they are selling. As of right now there was not enough data to properly predict and model the information across time, and internal data such as categorized loss leaders, could assist in mitigating the losses of the company by being more selective with brand or product offerings. 

Moving forward the company should try to modify their products offerings to a more limited portfolio in the areas where they are suffering losses, and expand on the areas, such as Accessories, where they are showing the highest profits. 




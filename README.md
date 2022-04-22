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
For exploration we used only our train dataframe. The explore.py file contains a number of functions that were used to help gain insights into our data, using both visual and statistical methods. We delved out the key factors shown to impact log error and our train, validate, and test dataframes only include these features. 

#### Clustering
A large component of our exploration was the use of clustering to help identify key drivers of log error. Clustering on geographical and continuous features provided insights into which clusters are most impactful, and allowed for the dataframes to be further trimmed to only the most optimal features to use for modeling. 

The main takeaways from exploration are that log error is influenced by: 
- bathrooms
- bedrooms
- squarefeet
- num_fireplace
- threequarter_baths
- logerror (target)
- age
- has_pool 
- tax_delinquency
- lat_long_cluster (cluster based on latitude and longitude)
- conts_cluster (cluster based on bathrooms, bedrooms, squarefeet, and age)
- age_sqft_cluster (cluster based on age and squarefeet)
- regionidzip (39 unique encoded zip codes)

### Modeling 
We created a number of models that included Ordinary Least Squares (OLS), Lasso & Lars, Polynomial Regression (using LinearRegression), and a Generalized Linear Model (GLM, using TweedieRegressor) types using our selected feature sets. Showing the result of all four, the OLS and Tweedie models performed nearly identical, and the Tweedie was selected for use with the test dataframe since it performed the best previously on a regression model to find tax value for a home. Our test ended up performing worse than the baseline, and ultimately only the train data for all of the models beat the baseline. None of the validate data did. 

### Deliverables 
The main deliverable from this project are the Final Report. Additionally there are modules that contain the functions used and workbooks where a deeper exploration of the process can be seen.

#### Final Report
The Final Report can be ran to reproduce the same results from start to finish. 

#### Modules
The modules included in this project are:
- wrangle_zillow.py
- explore.py
- modeling.py

#### Predictions
The modeling.py module could be used/modified to show predictions and contains functions that alter the train, validate, and test dataframes to store the outcomes from the models. More specifically the y component (target variable) has the predictions added to their respective dataframes.

### Summary and Recommendations
Ultimately we were not successful in identifying drivers that were capable of creating a useful, or even superior, regression model to that of a baseline guess. While we were able to gather features that were deemed statistically significant enough to use for modeling, they were not able to result in a model that could be utilized by Zillow. 

The first recommendation I would provide is to gather better, or correct the available data. There are a lot of issues with the utility of the data as it currently sits on the SQL server, but utltimately new features are needed to provide a model that obtains the goals set out in the project. While house features may contribute enough to the value of a house to be used successfully to predict value (Regression Project prior to this project), they are not useful enough in predicting the log error produced by Zillow for predicting said value. Perhaps for this data that centers around the 'hidden' bonuses of a house should be gathered, such as proximity to schools, quality of nearby businesses, and if there is or is not an HOA. (As some examples)

Moving forward one could spend more time with the data that is currently available but a better solution is probably to work to obtain features that are not currently present. 




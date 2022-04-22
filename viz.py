import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import wrangle_superstore as w
from datetime import date
from matplotlib import style

style.use("ggplot")


def graph_profit_by_category(df):
    """
    This function graphs the profit by category
    """
    # create a new dataframe with the category and profit
    df_cat_profit = (
        df.groupby("category").profit.sum().sort_values(ascending=False).head(10)
    )
    # create a bar plot
    df_cat_profit.plot(kind="bar")
    # add a title
    plt.title("Profit by Category")
    # add a label to the y-axis
    plt.ylabel("Profit")
    # add a label to the x-axis
    plt.xlabel("Category")
    # adjust rotation of the x-axis labels
    plt.xticks(rotation=45)
    # convert y-axis to dollars
    ax = plt.gca()
    ax.yaxis.set_major_formatter("${x:,.0f}")
    # add line at 0
    plt.axhline(y=0, color="grey")
    # show the plot
    plt.show()


def graph_quantity_by_category(df):
    """
    This function graphs the quantity by category
    """
    # create a new dataframe with the category and quantity
    df_cat_quantity = (
        df.groupby("category").quantity.sum().sort_values(ascending=False).head(10)
    )
    # create a bar plot
    df_cat_quantity.plot(kind="bar")
    # add a title
    plt.title("Quantity by Category")
    # add a label to the y-axis
    plt.ylabel("Quantity")
    # add a label to the x-axis
    plt.xlabel("Category")
    # adjust rotation of the x-axis labels
    plt.xticks(rotation=45)
    # convert y-axis to dollars
    ax = plt.gca()
    ax.yaxis.set_major_formatter("${x:,.0f}")
    # add line at 0
    plt.axhline(y=0, color="grey")
    # show the plot
    plt.show()


def graph_quantity_by_category_segment(df):
    """
    This function graphs the quantity by category and segment
    """
    # split df consumer, corporate, and home_office
    df_consumer = df[df.segment == "Consumer"]
    df_corporate = df[df.segment == "Corporate"]
    df_home_office = df[df.segment == "Home Office"]
    # combine above into a single df
    segment_quantity_df = pd.DataFrame()
    segment_quantity_df["consumer_quantity"] = (
        df_consumer.groupby("category")
        .quantity.sum()
        .sort_values(ascending=False)
        .head(10)
    )
    segment_quantity_df["corporate_quantity"] = (
        df_corporate.groupby("category")
        .quantity.sum()
        .sort_values(ascending=False)
        .head(10)
    )
    segment_quantity_df["home_office_quantity"] = (
        df_home_office.groupby("category")
        .quantity.sum()
        .sort_values(ascending=False)
        .head(10)
    )
    segment_quantity_df.plot(kind="bar", stacked=True)
    # remove x-axis title
    plt.xlabel("")
    # convert y-axis to dollars
    ax = plt.gca()
    ax.yaxis.set_major_formatter("${x:,.0f}")


def graph_profit_by_category_segment(df):
    """
    This function graphs the profit by category and segment
    """
    # split df consumer, corporate, and home_office
    df_consumer = df[df.segment == "Consumer"]
    df_corporate = df[df.segment == "Corporate"]
    df_home_office = df[df.segment == "Home Office"]
    # combine above into a single df
    segment_profit_df = pd.DataFrame()
    segment_profit_df["consumer_profit"] = (
        df_consumer.groupby("category")
        .profit.sum()
        .sort_values(ascending=False)
        .head(10)
    )
    segment_profit_df["corporate_profit"] = (
        df_corporate.groupby("category")
        .profit.sum()
        .sort_values(ascending=False)
        .head(10)
    )
    segment_profit_df["home_office_profit"] = (
        df_home_office.groupby("category")
        .profit.sum()
        .sort_values(ascending=False)
        .head(10)
    )
    # add a row for total
    segment_profit_df.loc["total"] = segment_profit_df.sum()
    segment_profit_df.plot(kind="bar", stacked=True)
    # change x axis rotation
    plt.xticks(rotation=45)
    # add title
    plt.title("Profit by Category and Segment")
    # ser y ticks to be in dollars
    # add line at 0
    plt.axhline(y=0, color="grey")
    # remove x-axis title
    plt.xlabel("")
    # convert y-axis to dollars
    ax = plt.gca()
    ax.yaxis.set_major_formatter("${x:,.0f}")


def graph_quarterly_profit(df, sub_category):
    """
    This function graphs the quarterly profit by category and segment
    """
    # make a temp df of quarterly profit for sub_category
    temp_df = df[df.sub_category == sub_category].resample("3M").sum()
    # make date column to assist in ordinal plotting
    temp_df["date"] = temp_df.index
    # make ordinal date column
    temp_df["ordinal"] = temp_df["date"].apply(lambda date: date.toordinal())
    # make the plot
    ax = sns.regplot(data=temp_df, x="ordinal", y="profit", line_kws={"color": "blue"},)
    # fix the x-axis labels
    ax.set_xlabel("date")
    new_labels = [date.fromordinal(int(item)) for item in ax.get_xticks()]
    ax.set_xticklabels(new_labels)
    # rotate x labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    # set title
    ax.set_title(f"Quarterly profits for : {sub_category}")
    # Change y label to dollars
    ax.yaxis.set_major_formatter("${x:,.0f}")
    plt.show()


def graph_top_and_bottom_sub_categories(df):
    """
    This function graphs the top and bottom sub categories
    """
    # which 3 sub_category have the highest profit?
    top = (
        df.groupby("sub_category")
        .sum()["profit"]
        .sort_values(ascending=False)
        .head(3)
        .index.tolist()
    )
    # which 3 sub_category have the lowest profit?
    bottom = (
        df.groupby("sub_category")
        .sum()["profit"]
        .sort_values(ascending=False)
        .tail(3)
        .index.tolist()
    )
    # add them together
    sub_categories = top + bottom
    for sub_category in sub_categories:
        plt = (
            df[df.sub_category == sub_category]
            .resample("3M")
            .sum()["profit"]
            .plot(label=sub_category, figsize=(12, 8), linewidth=4, ylim=(-1500, 2700),)
        )
    plt.axhline(y=0, color="black", linestyle="--")
    plt.legend(loc="lower left")


def avg_acc_brands(df):
    '''
    This function outputs a graph of the selected (through exploration) key brands to consider for average profit or loss outcomes for accessories. 
    The only input is the df and there is no return.
    '''
    _list = ['Plantronics', 'Maxell', 'Razer', 'Case', 'Logitech', 'Case', 'V7', 'NETGEAR']
    plt.figure(figsize=(16,13))
    sns.barplot(x= 'brand', y = 'profit', data = df[(df.sub_category == 'Accessories') & (df.brand.isin(_list))]  , ci=None)
    plt.xlabel('Product Line')
    plt.ylabel('Profit')
    plt.title('Major Accessory Profit/Loss by Brand')
    plt.xticks(rotation=90)
    plt.show()

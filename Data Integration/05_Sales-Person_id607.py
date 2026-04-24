# Problem ID: 607
# Title: Sales Person
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given three tables - SalesPerson (sales_id, name, salary, commission_rate, hire_date),
# Company (com_id, name, city), and Orders (order_id, order_date, com_id, sales_id, amount),
# find the names of all salespersons who did NOT have any orders
# related to the company named "RED".
#
# Approach:
# - Filter Company table to get com_id(s) where name == "RED"
# - Find all sales_ids in Orders that have orders with RED's com_id
# - Exclude those sales_ids from the SalesPerson table using ~ (NOT) + isin()
# - Select only required column:
#       ['name']

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get com_id(s) of RED — safely, without .values[0]
    red_ids = company[company['name'] == 'RED']['com_id']

    # Step 2: Find all sales_ids who have orders with RED
    sold_to_red = orders[orders['com_id'].isin(red_ids)]['sales_id'].unique()

    # Step 3: Exclude those salespeople
    result = sales_person[~sales_person['sales_id'].isin(sold_to_red)]

    return result[['name']]

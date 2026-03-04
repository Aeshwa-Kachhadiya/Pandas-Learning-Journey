# Problem ID: 183
# Title: Customers Who Never Order
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all customers who never ordered anything.
#
# A customer is considered valid if:
#   1) Their id does NOT appear in the Orders table
#
# Task:
# Return a DataFrame containing only the 'Customers' column
# with the names of customers who never placed an order.
#
# Approach:
# - Use isin() to check which customer ids appear in Orders
# - Apply NOT (~) operator to find customers with NO orders
# - Select only the required column:
#       ['name']
# - Rename column to 'Customers' as required by the problem

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])]
    return result[['name']].rename(columns={'name': 'Customers'})

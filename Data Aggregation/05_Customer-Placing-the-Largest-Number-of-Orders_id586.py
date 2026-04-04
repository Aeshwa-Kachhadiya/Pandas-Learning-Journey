# Problem ID: 586
# Title: Customer Placing the Largest Number of Orders
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find the customer_number for the customer who has placed the largest number of orders.
#
# Table: Orders
#   - order_number    (int) → Primary Key
#   - customer_number (int)
#
# Task:
# Return a DataFrame with only the customer_number column
# for the customer who has placed the most orders.
# Exactly one customer will always have the highest order count.
#
# Approach:
# - Use value_counts() on 'customer_number' to count orders per customer
# - Use idxmax() to get the customer_number with the highest count
# - Wrap the result in pd.DataFrame() since output must be a DataFrame
# - Return only [['customer_number']]

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders['customer_number'].value_counts().idxmax()
    return pd.DataFrame({'customer_number': [result]})

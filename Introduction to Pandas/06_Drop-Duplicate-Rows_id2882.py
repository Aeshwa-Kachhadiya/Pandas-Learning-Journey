# Problem ID: 2882
# Title: Drop Duplicate Rows
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame customers with columns:
#   - customer_id  (int)
#   - name         (object)
#   - email        (object)
#
# Remove duplicate rows based on the 'email' column,
# keeping only the first occurrence of each duplicate.
#
# Approach:
# - Use DataFrame.drop_duplicates() to remove duplicate rows
# - subset=['email'] ensures duplicates are checked on email column only
# - By default, keep='first' retains the first occurrence
# - Assigns the result back to customers and returns it

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=['email'])
    return customers

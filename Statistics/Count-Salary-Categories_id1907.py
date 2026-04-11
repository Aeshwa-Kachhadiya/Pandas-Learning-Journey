# Problem ID: 1907
# Title: Count Salary Categories
# Platform: LeetCode
# Difficulty: Medium
#
# Problem Statement:
# Given a table of bank accounts with monthly income,
# calculate the number of accounts in each salary category:
#   1) "Low Salary"     : income strictly less than $20,000
#   2) "Average Salary" : income in the inclusive range [$20,000, $50,000]
#   3) "High Salary"    : income strictly greater than $50,000
#
# Note: All three categories must appear in the result.
#       If no accounts fall in a category, return 0.
#
# Approach:
# - Define a categorize() helper and apply it to each row
#   to create a new 'category' column
# - Use value_counts() to count occurrences per category
# - Create a reference DataFrame with all 3 categories
# - Left join counts onto it so missing categories default to 0
# - Fill NaN with 0 using fillna(0)

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    # Step 1: Assign a category to each row
    def categorize(income):
        if income < 20000:
            return 'Low Salary'
        elif income <= 50000:
            return 'Average Salary'
        else:
            return 'High Salary'

    accounts['category'] = accounts['income'].apply(categorize)

    # Step 2: Count each category
    counts = accounts['category'].value_counts().reset_index()
    counts.columns = ['category', 'accounts_count']

    # Step 3: Ensure all 3 categories are present (even if count is 0)
    all_categories = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary']})
    result = all_categories.merge(counts, on='category', how='left').fillna(0)

    return result

# Problem ID: 1484
# Title: Group Sold Products By The Date
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# For each date find the number of different products sold and their names.
# Product names should be sorted lexicographically and returned as a comma separated string.
#
# Table: Activities
#   - sell_date  (date)
#   - product    (varchar)
# No primary key, table may contain duplicates.
#
# Task:
# Return a DataFrame with sell_date, num_sold and products columns
# ordered by sell_date.
#
# Approach:
# - Group by 'sell_date' to aggregate per date
# - Use agg() to compute two things at once:
#     - num_sold  → nunique() to count distinct products per date
#     - products  → sorted() + ','.join() to combine names alphabetically into one string
# - Use reset_index() to bring sell_date back as a normal column
# - Return result with all three columns

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = activities.groupby('sell_date').agg(
        num_sold=('product', 'nunique'),
        products=('product', lambda x: ','.join(sorted(x.unique())))
    ).reset_index()

    return result

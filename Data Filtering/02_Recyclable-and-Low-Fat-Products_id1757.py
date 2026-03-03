# Problem ID: 1757
# Title: Recyclable and Low Fat Products
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find the ids of products that are both low fat and recyclable.
#
# A product is considered valid if:
#   1) low_fats = 'Y'
#   2) recyclable = 'Y'
#
# Task:
# Return a DataFrame containing only the product_id
# of products that satisfy both conditions.
#
# Approach:
# - Use boolean indexing to filter rows
# - Apply AND condition:
#       low_fats == 'Y'
#       AND
#       recyclable == 'Y'
# - Select only the required column:
#       ['product_id']

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result = products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    ]
    
    return result[['product_id']]

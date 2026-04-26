# Problem ID: 1795
# Title: Rearrange Products Table
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a Products table with product_id and three store columns
# (store1, store2, store3), rearrange the table so that each row
# has (product_id, store, price).
# If a product is not available in a store (null price),
# do not include that row in the result.
#
# Task:
# Convert the wide format table into a long format table with
# columns: product_id, store, price.
# Exclude rows where price is null.
#
# Approach:
# - Use melt() to convert wide format to long format:
#       id_vars='product_id'         → column to keep as is
#       value_vars=['store1',...]    → columns to melt into rows
#       var_name='store'             → name for the new store column
#       value_name='price'           → name for the new price column
# - Use dropna() to remove rows where price is null
#   (product not available in that store)
# - Return the resulting DataFrame

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = products.melt(
        id_vars='product_id',
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )
    result = result.dropna(subset=['price'])
    return result

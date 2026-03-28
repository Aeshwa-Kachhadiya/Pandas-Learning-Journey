# Problem ID: 2887
# Title: Fill Missing Data
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame products with columns:
#   - name      (object)
#   - quantity  (int)
#   - price     (int)
#
# Fill all missing values (NaN) in the 'quantity' column with 0.
#
# Approach:
# - Use Series.fillna() to replace NaN values with a specified value
# - fillna(0) replaces all NaN entries in 'quantity' with 0
# - Directly overwrites the existing 'quantity' column
# - Other common fillna() strategies (for reference):
#       fillna(df['col'].mean())    → fill with column mean
#       fillna(df['col'].median())  → fill with column median
#       fillna(method='ffill')      → forward fill from previous row
#       fillna(method='bfill')      → backward fill from next row

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

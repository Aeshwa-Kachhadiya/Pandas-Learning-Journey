# Problem ID: 2888
# Title: Reshape Data: Concatenate
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given two DataFrames df1 and df2, both with columns:
#   - student_id  (int)
#   - name        (object)
#   - age         (int)
#
# Concatenate the two DataFrames vertically into one DataFrame
# (stack df2 rows below df1 rows).
#
# Approach:
# - Use pd.concat() to combine the two DataFrames
# - Pass both DataFrames as a list: [df1, df2]
# - axis=0 means vertical concatenation (row-wise)
#       axis=0 → stack rows vertically   (add more rows)
#       axis=1 → stack columns horizont. (add more columns)
# - Note: resulting DataFrame may have duplicate index values
#   use reset_index(drop=True) if a clean index is needed:
#       pd.concat([df1, df2], axis=0).reset_index(drop=True)

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df1, df2], axis=0)
    return df

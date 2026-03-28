# Problem ID: 2883
# Title: Drop Missing Data
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame students with columns:
#   - student_id  (int)
#   - name        (object)
#   - age         (int)
#
# Remove all rows where the 'name' column has missing values (NaN).
#
# Approach:
# - Use Series.notna() to create a boolean mask
#       True  → name has a valid value
#       False → name is NaN/missing
# - Apply the mask to filter out rows where name is missing
# - students[students['name'].notna()] keeps only non-null name rows
# - Assigns the result back to students and returns it

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students = students[students['name'].notna()]
    return students

# Problem ID: 2881
# Title: Create a New Column
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame employees with columns:
#   - name    (object)
#   - salary  (int)
#
# Create a new column 'bonus' that contains the doubled
# values of the salary column (bonus = salary * 2).
#
# Approach:
# - Directly assign a new column using bracket notation
# - Multiply the entire 'salary' column by 2 using vectorized operation
# - employees['bonus'] = employees['salary'] * 2
# - Return the updated DataFrame with the new column added

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

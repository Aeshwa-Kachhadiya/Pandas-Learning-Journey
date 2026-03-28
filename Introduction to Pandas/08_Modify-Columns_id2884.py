# Problem ID: 2884
# Title: Modify Columns
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame employees with columns:
#   - name    (object)
#   - salary  (int)
#
# Modify the existing 'salary' column by multiplying
# each salary value by 2 (double every employee's salary).
#
# Approach:
# - Directly overwrite the existing 'salary' column
# - Multiply the entire column by 2 using vectorized operation
# - employees['salary'] = employees['salary'] * 2
# - Unlike Problem 2881 (which ADDED a new 'bonus' column),
#   this problem MODIFIES the existing 'salary' column in place
# - Return the updated DataFrame

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

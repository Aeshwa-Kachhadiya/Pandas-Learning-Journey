# Problem ID: 2879
# Title: Display the First Three Rows
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame employees with columns:
#   - employee_id  (int)
#   - name         (object)
#   - department   (object)
#   - salary       (int)
#
# Display the first 3 rows of the DataFrame.
#
# Approach:
# - DataFrame.head(n) returns the first n rows
# - head(3) directly returns the first 3 rows
# - Maintains original column structure and order

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

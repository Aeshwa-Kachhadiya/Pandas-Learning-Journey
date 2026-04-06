# Problem ID: 176
# Title: Second Highest Salary
# Platform: LeetCode
# Difficulty: Medium
#
# Problem Statement:
# Given an Employee table with columns:
#   - id (int): Primary key, unique identifier for each employee
#   - salary (int): Salary of the employee
#
# Task:
# Find the second highest DISTINCT salary from the Employee table.
# If there is no second highest salary, return null (None in Pandas).
#
# Approach:
# - Extract unique salaries using .unique()
# - Sort them in descending order using sorted(..., reverse=True)
# - Check if at least 2 distinct salaries exist:
#       If not → return DataFrame with None
#       If yes → return the element at index [1] (second highest)
# - Return result as DataFrame with column name 'SecondHighestSalary'

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get unique salaries sorted highest to lowest
    unique_salaries = sorted(employee['salary'].unique(), reverse=True)

    # Check if second highest exists
    if len(unique_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})

    return pd.DataFrame({'SecondHighestSalary': [unique_salaries[1]]})

# Problem ID: 177
# Title: Nth Highest Salary
# Platform: LeetCode
# Difficulty: Medium
#
# Problem Statement:
# Find the nth highest distinct salary from the Employee table.
# If there are less than n distinct salaries, return null.
#
# Table: Employee
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key for this table.
#
# Approach:
# - Drop duplicates to get distinct salaries
# - Sort in descending order (highest first)
# - Validate: if N <= 0 or fewer than N distinct salaries exist, return None
# - Use iloc[N-1] to fetch the Nth salary (0-based indexing)
# - Return as DataFrame with dynamic column name: getNthHighestSalary(N)

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Step 1: Get all unique/distinct salaries
    distinct_salaries = employee['salary'].drop_duplicates()

    # Step 2: Sort them in descending order (highest first)
    sorted_salaries = distinct_salaries.sort_values(ascending=False)

    # Step 3: Pick the Nth one (using index N-1)
    # If there are fewer than N distinct salaries, return null
    if len(sorted_salaries) < N or N <= 0:
        result = None
    else:
        result = sorted_salaries.iloc[N - 1]  # iloc is 0-based, so Nth = index N-1

    # Step 4: Return as a DataFrame with the exact required column name
    col_name = f"getNthHighestSalary({N})"
    return pd.DataFrame({col_name: [result]})

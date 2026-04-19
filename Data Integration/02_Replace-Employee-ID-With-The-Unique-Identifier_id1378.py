# Problem ID: 1378
# Title: Replace Employee ID With The Unique Identifier
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given two tables - Employees (id, name) and EmployeeUNI (id, unique_id),
# show the unique ID of each employee.
# If an employee does not have a unique ID, show null instead.
#
# Approach:
# - Use a LEFT JOIN (merge) on 'id' to keep all employees
# - Employees without a matching unique_id will automatically get NaN (null)
# - Select only required columns:
#       ['unique_id', 'name']

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Left merge — keep all employees, match unique_id if exists
    result = employees.merge(employee_uni, on='id', how='left')

    # Return only required columns
    return result[['unique_id', 'name']]

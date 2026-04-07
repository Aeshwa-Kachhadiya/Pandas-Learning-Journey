# Problem ID: 184
# Title: Department Highest Salary
# Platform: LeetCode
# Difficulty: Medium
#
# Problem Statement:
# Given an Employee table with columns:
#   - id (int): Primary key, unique identifier for each employee
#   - name (varchar): Name of the employee
#   - salary (int): Salary of the employee
#   - departmentId (int): Foreign key referencing the Department table
#
# Given a Department table with columns:
#   - id (int): Primary key, unique identifier for each department
#   - name (varchar): Name of the department
#
# Task:
# Find the employees who have the highest salary in each department.
# Return the result with columns: Department, Employee, Salary
# Return the result table in any order.
#
# Approach:
# - Merge Employee and Department tables on departmentId = id
#       to bring department name alongside employee info
# - Use groupby + transform('max') on 'salary' grouped by 'departmentId'
#       to compute the max salary per department for every row
# - Filter rows where the employee's salary equals the department max salary
# - Rename and return only the required columns:
#       'name_dept' → 'Department', 'name_emp' → 'Employee', 'salary' → 'Salary'

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Merge both tables to get department name alongside employee info
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))

    # Step 2: Find the max salary for each department
    max_salaries = merged.groupby('departmentId')['salary'].transform('max')

    # Step 3: Keep only rows where salary == max salary of that department
    result = merged[merged['salary'] == max_salaries]

    # Step 4: Return only the required columns with correct names
    return result[['name_dept', 'name_emp', 'salary']].rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })

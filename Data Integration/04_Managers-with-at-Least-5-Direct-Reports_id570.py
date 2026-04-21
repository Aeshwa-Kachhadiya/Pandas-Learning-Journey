# Problem ID: 570
# Title: Managers with at Least 5 Direct Reports
# Platform: LeetCode
# Difficulty: Medium
#
# Problem Statement:
# Given an Employee table (id, name, department, managerId),
# find all managers who have at least 5 direct reports.
# If managerId is null, the employee has no manager.
# Return only the names of qualifying managers.
#
# Approach:
# - Group by managerId and count how many employees report to each manager
# - Filter managers with report_count >= 5
# - Merge back with the Employee table using managerId == id
#   to retrieve the actual name of the manager
# - Select only required column:
#       ['name']

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Count direct reports per managerId
    report_counts = employee.groupby('managerId')['id'].count().reset_index()
    report_counts.columns = ['managerId', 'report_count']

    # Step 2: Filter managers with at least 5 direct reports
    qualified = report_counts[report_counts['report_count'] >= 5]

    # Step 3: Merge back using managerId matching to employee's id
    result = qualified.merge(employee[['id', 'name']],
                             left_on='managerId',   # ← key fix!
                             right_on='id',
                             how='inner')

    return result[['name']]

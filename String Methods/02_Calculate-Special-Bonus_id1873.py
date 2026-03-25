# Problem ID: 1873
# Title: Calculate Special Bonus
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Calculate the bonus for each employee based on the following conditions:
#
# An employee receives 100% of their salary as bonus if:
#   1) Their employee_id is an odd number, AND
#   2) Their name does NOT start with the character 'M'
# Otherwise, the bonus is 0.
#
# Task:
# Return a DataFrame with 'employee_id' and 'bonus' columns
# sorted in ascending order by employee_id.
#
# Approach:
# - Use np.where() to apply conditional logic vectorized across the DataFrame
# - Condition: (employee_id % 2 == 1) AND (name does not start with 'M')
# - If True  → bonus = salary
# - If False → bonus = 0
# - Select 'employee_id' and 'bonus', sort by 'employee_id'

import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = np.where(
        (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M')),
        employees['salary'],
        0
    )
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')

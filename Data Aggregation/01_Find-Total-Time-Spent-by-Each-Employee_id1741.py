# Problem ID: 1741
# Title: Find Total Time Spent by Each Employee
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a table of employee office entry/exit events,
# calculate the total time in minutes spent by each employee
# on each day at the office.
# An employee can enter and leave more than once per day.
# The time spent for a single entry is: out_time - in_time.
#
# Task:
# Return a DataFrame containing the day, emp_id,
# and total time spent at the office per employee per day.
#
# Approach:
# - Compute time spent per entry:
#       total_time = out_time - in_time
# - Group by ['event_day', 'emp_id'] and sum 'total_time'
# - Rename 'event_day' column to 'day'

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()
    result = result.rename(columns={'event_day': 'day'})
    return result

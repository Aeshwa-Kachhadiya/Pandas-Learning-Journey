# Problem ID: 2880
# Title: Select Data
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame students with columns:
#   - student_id  (int)
#   - name        (object)
#   - age         (int)
#
# Select the name and age of the student where student_id = 101.
#
# Approach:
# - Use boolean indexing to filter rows where student_id == 101
# - Select only the required columns ['name', 'age']
# - Chaining both operations in a single line:
#       students[students['student_id'] == 101][['name', 'age']]

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

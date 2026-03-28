# Problem ID: 2886
# Title: Change Data Type
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame students with columns:
#   - student_id  (int)
#   - name        (object)
#   - age         (int)
#   - grade       (float)
#
# The 'grade' column is incorrectly stored as float.
# Convert it to integer type.
#
# Approach:
# - Use Series.astype() to convert column data type
# - astype(int) truncates the decimal part (e.g. 9.0 → 9)
# - Directly overwrites the existing 'grade' column
# - Note: astype(int) will raise an error if the column
#   contains NaN values — use astype('Int64') (nullable int)
#   if missing values are possible

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

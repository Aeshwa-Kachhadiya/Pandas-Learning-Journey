# Problem ID: 2885
# Title: Rename Columns
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame students with columns:
#   - id     (int)
#   - first  (object)
#   - last   (object)
#   - age    (int)
#
# Rename the columns as follows:
#   - id    → student_id
#   - first → first_name
#   - last  → last_name
#   - age   → age_in_years
#
# Approach:
# - Use DataFrame.rename() with a columns mapping dictionary
# - Pass old column names as keys, new names as values
# - Alternative approach (commented out):
#       students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
#       This directly reassigns all column names at once
#       BUT requires knowing the exact order of all columns
#       rename() is safer as it only targets specified columns

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={
        'id'    : 'student_id',
        'first' : 'first_name',
        'last'  : 'last_name',
        'age'   : 'age_in_years'
    })
    # Alternative: students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
    return students

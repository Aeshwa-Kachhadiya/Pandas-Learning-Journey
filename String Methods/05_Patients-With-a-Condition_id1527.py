# Problem ID: 1527
# Title: Patients With a Condition
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all patients who have Type I Diabetes.
# Type I Diabetes is identified by a condition code that starts with the prefix 'DIAB1'.
#
# A valid patient satisfies:
#   1) Their 'conditions' field contains at least one code starting with 'DIAB1'
#   2) 'DIAB1' must appear either at the start of the string OR after a space
#      (to avoid partial matches like 'XDIAB1')
#
# Task:
# Return a DataFrame with 'patient_id', 'patient_name', and 'conditions' columns
# in any order.
#
# Approach:
# - Use str.contains() with a regex pattern to match valid DIAB1 occurrences
# - Regex breakdown:
#     (^|(?<=\s))  → DIAB1 must be at the start of string OR preceded by a space
#     DIAB1        → the required prefix for Type I Diabetes codes
# - This prevents false positives where 'DIAB1' appears mid-word (e.g., 'XDIAB1')

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(^|(?<=\s))DIAB1', regex=True)]

# Problem ID: 2877
# Title: Create a DataFrame from List
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a 2D list called student_data containing IDs and ages
# of some students, create a DataFrame with two columns:
#   - student_id
#   - age
# The DataFrame should maintain the same order as the original list.
#
# Approach:
# - Use pd.DataFrame() constructor directly on the 2D list
# - Pass column names as ['student_id', 'age']
# - Each inner list [id, age] becomes one row in the DataFrame

import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(
        student_data,
        columns=['student_id', 'age']
    )

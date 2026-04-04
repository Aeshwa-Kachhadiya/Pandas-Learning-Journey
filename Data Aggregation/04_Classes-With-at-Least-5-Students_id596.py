# Problem ID: 596
# Title: Classes With at Least 5 Students
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all the classes that have at least five students.
#
# Table: Courses
#   - student  (varchar)
#   - class    (varchar)
# (student, class) is the primary key
#
# Task:
# Return a DataFrame with only the class column
# where the class has 5 or more students enrolled.
# Result can be in any order.
#
# Approach:
# - Group by 'class' to aggregate per class
# - Use filter() with lambda to keep only groups where len(x) >= 5
# - Select only the 'class' column
# - Use drop_duplicates() to remove duplicate class names
# - Return only [['class']]

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby('class').filter(lambda x: len(x) >= 5)[['class']].drop_duplicates()
    return result[['class']]

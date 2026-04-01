# Problem ID: 2356
# Title: Number of Unique Subjects Taught by Each Teacher
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Calculate the number of unique subjects each teacher teaches in the university.
#
# Table: Teacher
#   - teacher_id  (int)
#   - subject_id  (int)
#   - dept_id     (int)
# (subject_id, dept_id) is the primary key
#
# Task:
# Return a DataFrame with teacher_id and the count of unique subjects (cnt).
# Result can be in any order.
#
# Approach:
# - Group by 'teacher_id' to aggregate per teacher
# - Use nunique() on 'subject_id' to count distinct subjects per teacher
# - Rename the aggregated column to 'cnt'
# - Reset index to bring teacher_id back as a column
# - Return only ['teacher_id', 'cnt']

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id')['subject_id'].nunique().rename('cnt').reset_index()
    return result[['teacher_id', 'cnt']]

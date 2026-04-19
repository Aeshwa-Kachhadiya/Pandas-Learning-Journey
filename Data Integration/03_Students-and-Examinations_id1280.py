# Problem ID: 1280
# Title: Students and Examinations
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given three tables - Students (student_id, student_name),
# Subjects (subject_name), and Examinations (student_id, subject_name),
# find the number of times each student attended each exam.
# Return the result ordered by student_id and subject_name.
#
# Approach:
# - CROSS JOIN Students and Subjects to get all possible combinations
# - Group Examinations by (student_id, subject_name) and count occurrences
# - LEFT JOIN the counts into all combinations so missing exams show 0
# - Fill NaN with 0, cast to int, and sort by student_id and subject_name
# - Select only required columns:
#       ['student_id', 'student_name', 'subject_name', 'attended_exams']

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Cross join — every student paired with every subject
    all_combinations = students.merge(subjects, how='cross')

    # Step 2: Count how many times each student attended each exam
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index()
    exam_counts.columns = ['student_id', 'subject_name', 'attended_exams']

    # Step 3: Left merge to bring counts into all combinations
    result = all_combinations.merge(exam_counts, on=['student_id', 'subject_name'], how='left')

    # Step 4: Fill missing counts with 0 and sort
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]\
                 .sort_values(['student_id', 'subject_name'])

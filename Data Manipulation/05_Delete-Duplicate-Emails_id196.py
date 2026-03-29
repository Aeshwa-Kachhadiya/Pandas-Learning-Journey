# Problem ID: 196
# Title: Delete Duplicate Emails
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a table of Person with id and email columns,
# delete all duplicate emails keeping only the one
# with the smallest id for each email.
#
# Task:
# Modify the Person DataFrame in place (no return value).
# Keep only one unique email with the smallest id.
#
# Approach:
# - Sort by 'id' in ascending order so smallest id comes first
# - Drop duplicates based on 'email' column keeping first occurrence
# - Both operations done inplace to modify original DataFrame directly
# - No return value as function signature is -> None

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)

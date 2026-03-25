# Problem ID: 1517
# Title: Find Users With Valid E-Mails
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all users who have valid email addresses.
#
# A valid email must satisfy:
#   1) Prefix starts with a letter (a-z or A-Z)
#   2) Prefix may contain letters, digits, underscore '_', period '.', or dash '-'
#   3) Domain must be exactly '@leetcode.com'
#
# Task:
# Return a DataFrame with all columns for users whose email is valid,
# in any order.
#
# Approach:
# - Use str.match() with a regex pattern to validate each email
# - Regex breakdown:
#     ^[A-Za-z]       → prefix must start with a letter
#     [A-Za-z0-9_.-]* → followed by any valid prefix characters (0 or more)
#     @leetcode\.com$ → domain must be exactly @leetcode.com
# - na=False ensures NaN emails are treated as invalid (not raising errors)

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    filtered_df = users[
        users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$', na=False)
    ]
    return filtered_df

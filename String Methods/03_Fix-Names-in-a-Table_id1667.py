# Problem ID: 1667
# Title: Fix Names in a Table
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Fix the names in the Users table so that only the first character is uppercase
# and the rest of the characters are lowercase.
#
# A valid fixed name satisfies:
#   1) First character is uppercase
#   2) All remaining characters are lowercase
#
# Task:
# Return a DataFrame with 'user_id' and 'name' columns
# sorted in ascending order by user_id.
#
# Approach:
# - Use str.capitalize() to convert the first character to uppercase
#   and the rest to lowercase in one step
# - Sort by 'user_id' using sort_values()

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')

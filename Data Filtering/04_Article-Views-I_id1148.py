# Problem ID: 1148
# Title: Article Views I
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all authors who viewed at least one of their own articles.
#
# A valid author is:
#   1) Someone whose author_id == viewer_id (they viewed their own article)
#
# Task:
# Return a DataFrame containing only the 'id' column
# sorted in ascending order with no duplicates.
#
# Approach:
# - Filter rows where author_id == viewer_id (same person)
# - Select only 'author_id' column and rename it to 'id'
# - Remove duplicates using drop_duplicates() (same author may appear multiple times)
# - Sort by 'id' in ascending order using sort_values()

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = views[views['author_id'] == views['viewer_id']]
    return result[['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates().sort_values('id')

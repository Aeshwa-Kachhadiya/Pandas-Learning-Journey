# Problem ID: 1683
# Title: Invalid Tweets
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all tweet IDs where the content length is strictly greater than 15 characters.
#
# A tweet is invalid if:
#   1) The number of characters in 'content' is strictly greater than 15
#
# Task:
# Return a DataFrame containing only the 'tweet_id' column
# in any order.
#
# Approach:
# - Use str.len() to compute the length of each tweet's content
# - Filter rows where content length > 15
# - Select only the 'tweet_id' column and return

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    result = tweets[tweets['content'].str.len() > 15]
    return result[['tweet_id']]

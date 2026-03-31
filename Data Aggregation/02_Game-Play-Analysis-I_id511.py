# Problem ID: 511
# Title: Game Play Analysis I
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a table of player activity logs,
# find the first login date for each player.
# A player can have multiple login records on different dates.
#
# Task:
# Return a DataFrame containing the player_id
# and their earliest login date as 'first_login'.
#
# Approach:
# - Group by 'player_id' and find the minimum 'event_date'
#       (min gives the earliest/first date per player)
# - Reset index to bring player_id back as a normal column
# - Rename 'event_date' to 'first_login'

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id')['event_date'].min().reset_index()
    return activity.rename(columns={'event_date': 'first_login'})

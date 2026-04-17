# Problem ID: 1050
# Title: Actors and Directors Who Cooperated At Least Three Times
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Find all the pairs (actor_id, director_id)
# where an actor has cooperated with the same
# director at least three times.
#
# Table: ActorDirector
#   - actor_id     (int)
#   - director_id  (int)
#   - timestamp    (int)
# timestamp is the primary key.
#
# Task:
# Return a DataFrame with:
#   - actor_id
#   - director_id
# where each pair appears at least 3 times.
# Result can be in any order.
#
# Approach:
# - Count occurrences of each (actor_id, director_id) pair
#   using value_counts()
# - Convert counts to DataFrame using reset_index()
# - Filter rows where count >= 3
# - Return only actor_id and director_id columns

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = (
        actor_director[['actor_id', 'director_id']]
        .value_counts()
        .reset_index()
    )
    
    result = result[result['count'] >= 3]
    
    return result[['actor_id', 'director_id']]

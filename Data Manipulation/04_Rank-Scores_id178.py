# Problem ID: 178
# Title: Rank Scores
# Platform: LeetCode
# Difficulty: Medium
#
# Problem Statement:
# Rank the scores from highest to lowest.
# Rules:
#   1) Highest score gets rank 1
#   2) If two scores are equal, they get the SAME rank
#   3) After a tie, next rank is the next consecutive number
#      (no gaps in ranking)
#
# Task:
# Return a DataFrame with score and rank,
# ordered by score in descending order.
#
# Approach:
# - Use .rank() with method='dense' to handle ties without gaps
# - ascending=False because highest score = rank 1
# - Sort by score descending using sort_values()
# - Select only required columns: ['score', 'rank']

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Rank the scores using dense ranking
    # method='dense' → no gaps after ties (1,1,2 not 1,1,3)
    # ascending=False → highest score gets rank 1
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)

    # Step 2: Sort by score descending
    result = scores.sort_values('score', ascending=False)

    # Step 3: Return only required columns
    return result[['score', 'rank']]

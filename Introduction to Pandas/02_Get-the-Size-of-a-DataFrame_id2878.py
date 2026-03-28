# Problem ID: 2878
# Title: Get the Size of a DataFrame
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame players with columns:
#   - player_id  (int)
#   - name       (object)
#   - age        (int)
#   - position   (object)
#   - ...
#
# Calculate and display the number of rows and columns.
# Return the result as an array:
#   [number of rows, number of columns]
#
# Approach:
# - DataFrame.shape returns a tuple (rows, columns)
# - Convert it to a list using list()
# - list(players.shape) directly gives [num_rows, num_columns]

import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

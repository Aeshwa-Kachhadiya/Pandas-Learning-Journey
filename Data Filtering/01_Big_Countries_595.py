# Problem ID: 595
# Title: Big Countries
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# A country is considered "big" if:
#   1) Its area is at least 3,000,000 km², OR
#   2) Its population is at least 25,000,000.
#
# Task:
# Return a DataFrame containing the name, population,
# and area of all big countries.
#
# Approach:
# - Use boolean indexing to filter rows
# - Apply OR condition:
#       area >= 3000000
#       OR
#       population >= 25000000
# - Select only required columns:
#       ['name', 'population', 'area']

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = world[
        (world['area'] >= 3000000) |
        (world['population'] >= 25000000)
    ]
    
    return result[['name', 'population', 'area']]
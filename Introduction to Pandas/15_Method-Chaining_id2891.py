# Problem ID: 2891
# Title: Method Chaining
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame animals with columns:
#   - name     (object)
#   - species  (object)
#   - age      (int)
#   - weight   (int)
#
# Return the names of animals that weigh strictly more than
# 100 kilograms, sorted by weight in descending order.
#
# Approach:
# - Step 1: Filter rows where weight > 100 using boolean indexing
# - Step 2: Sort the filtered result by 'weight' descending
#       sort_values(by='weight', ascending=False)
# - Step 3: Select only the 'name' column
# - All 3 steps can be chained into one line (method chaining):
#       animals[animals['weight'] > 100]
#              .sort_values(by='weight', ascending=False)[['name']]
# - Method chaining keeps code concise and readable by
#   combining multiple DataFrame operations in a single expression
#   without creating intermediate variables

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals[animals['weight'] > 100]
    animals = animals.sort_values(by='weight', ascending=False)
    return animals[['name']]

    # Method chaining alternative (one-liner):
    # return animals[animals['weight'] > 100]\
    #        .sort_values(by='weight', ascending=False)[['name']]

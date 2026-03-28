# Problem ID: 2890
# Title: Reshape Data: Melt
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame report with columns:
#   - product    (object)
#   - quarter_1  (int)
#   - quarter_2  (int)
#   - quarter_3  (int)
#   - quarter_4  (int)
#
# Reshape the data so that each row represents sales data
# for a product in a specific quarter.
#
# Approach:
# - Use pd.melt() to reshape from wide to long format
#       id_vars    = 'product'                     → column to keep as identifier
#       value_vars = ['quarter_1' ... 'quarter_4'] → columns to unpivot into rows
#       var_name   = 'quarter'                     → name for the new variable column
#       value_name = 'sales'                       → name for the new values column
# - Wide format (original):                Long format (melted):
#       product | Q1 | Q2 | Q3 | Q4          product  | quarter   | sales
#       Phone   | 10 | 20 | 30 | 40    →     Phone    | quarter_1 | 10
#       Laptop  | 15 | 25 | 35 | 45          Phone    | quarter_2 | 20
#                                            Laptop   | quarter_1 | 15
#                                            Laptop   | quarter_2 | 25
# - melt() is the opposite of pivot() —
#   pivot() goes long → wide
#   melt()  goes wide → long

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = pd.melt(
        report,
        id_vars    = 'product',
        value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name   = 'quarter',
        value_name = 'sales'
    )
    return report

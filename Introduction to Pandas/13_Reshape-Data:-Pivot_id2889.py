# Problem ID: 2889
# Title: Reshape Data: Pivot
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# Given a DataFrame weather with columns:
#   - city         (object)
#   - month        (object)
#   - temperature  (int)
#
# Pivot the data so that:
#   - Each ROW    represents a specific month
#   - Each COLUMN represents a specific city
#   - Cell values represent the temperature
#
# Approach:
# - Use DataFrame.pivot() to reshape from long to wide format
#       index   = 'month'       → unique months become row labels
#       columns = 'city'        → unique cities become column names
#       values  = 'temperature' → fills the cell values
# - Long format (original):                Wide format (pivoted):
#       city   | month | temp         month | CityA | CityB
#       CityA  | Jan   | 20     →     Jan   |  20   |  15
#       CityB  | Jan   | 15           Feb   |  22   |  18
#       CityA  | Feb   | 22
#       CityB  | Feb   | 18
# - Note: pivot() requires unique (index, column) combinations
#   If duplicates exist, use pivot_table() with an aggfunc instead:
#       weather.pivot_table(index='month', columns='city',
#                           values='temperature', aggfunc='mean')

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df_weather = weather.pivot(
        index='month',
        columns='city',
        values='temperature'
    )
    return df_weather

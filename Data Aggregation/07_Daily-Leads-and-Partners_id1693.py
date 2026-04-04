# Problem ID: 1693
# Title: Daily Leads and Partners
# Platform: LeetCode
# Difficulty: Easy
#
# Problem Statement:
# For each date_id and make_name find the number of
# distinct lead_id's and distinct partner_id's.
#
# Table: DailySales
#   - date_id     (date)
#   - make_name   (varchar)
#   - lead_id     (int)
#   - partner_id  (int)
# No primary key, table may contain duplicates.
#
# Task:
# Return a DataFrame with date_id, make_name, unique_leads and unique_partners columns.
# Result can be in any order.
#
# Approach:
# - Group by both 'date_id' and 'make_name' by passing them as a list
# - Use agg() to compute two things at once:
#     - unique_leads    → nunique() on lead_id to count distinct leads
#     - unique_partners → nunique() on partner_id to count distinct partners
# - Use reset_index() to bring date_id and make_name back as normal columns
# - Return result with all four columns

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()

    return result

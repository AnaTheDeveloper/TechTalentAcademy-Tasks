# The .merge() method looks for columns that are common between two DataFrames and then looks for rows where
# those column’s values are the same. It then combines the matching rows into a single row in a new table.

# new_df = pd.merge(df_name1, df_name2) or new_df = df_name1.merge(df_name2)

# Chaining multiple dataframes
# big_df = orders.merge(customers)\.merge(products)

# pd.merge(
#     orders,
#     customers.rename(columns={'id': 'customer_id'}))

# Marge specific columns
# pd.merge(
#     orders,
#     customers,
#     left_on='customer_id',
#     right_on='id')

# Outer merge
# pd.merge(company_a, company_b, how='outer')

# Left and right merge
# pd.merge(company_a, company_b, how='left')
# pd.merge(company_a, company_b, how="right")

# Concatenate DataFrames
# pd.concat([df1, df2])

# READ MORE ON MERGING WITH PANDAS HERE: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html
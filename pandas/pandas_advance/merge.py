import pandas as pd

# merge

''' 
two dataframes, combine them using a common column.
python
'''
df_orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4],
    'customer_id': [101, 102, 103, 104],
    'amount': [500, 300, 700, 200]
})

df_customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})
# syntax:
'''
pythonpd.merge(left_df, right_df, on='common_column', how='join_type')
on — column that exists in both dataframes, used to match rows
how — which rows to keep
'''

# the data visually:
'''
df_orders          df_customers
cust_id            cust_id  name
101                101      Alice
102       ←→       102      Bob
103                103      Charlie
104                105      David
↑ no match         ↑ no match
'''
# inner — only rows that match on both sides:
pd.merge(df_orders, df_customers, on='customer_id', how='inner')
# keeps: 101, 102, 103
# 104 dropped, 105 dropped
# left — all rows from left df, match where possible from right:
pd.merge(df_orders, df_customers, on='customer_id', how='left')
# keeps: 101, 102, 103, 104
# 104 stays, name = NaN
# right — all rows from right df, match where possible from left:
pd.merge(df_orders, df_customers, on='customer_id', how='right')
# keeps: 101, 102, 103, 105
# 105 stays, order data = NaN
# outer — everything from both sides:
pd.merge(df_orders, df_customers, on='customer_id', how='outer')
# keeps: 101, 102, 103, 104, 105
# 104 → name = NaN
# 105 → order data = NaN

# summary:
'''
| how   | keeps                                    |
|-------|------------------------------------------|
| inner | only matching rows                       |
| left  | all of left + matches from right         |
| right | all of right + matches from left         |
| outer | everything from both                     |
'''
import pandas as pd

# pivot_table
'''
reshapes data — turns row values into columns. think of it like groupby but the output is a 2D table instead of a flat list.
'''

# example DataFrame:
df = pd.DataFrame({
    'region': ['North', 'South', 'North', 'South', 'North'],
    'product': ['A', 'A', 'B', 'B', 'A'],
    'sales': [100, 200, 150, 300, 120]
})

# syntax:
df.pivot_table(values='col_to_aggregate', index='row_labels', columns='col_labels', aggfunc='function')
'''
- values — column you want to aggregate
- index — what becomes the rows
- columns — what becomes the columns
- aggfunc — how to aggregate (sum, mean, count etc.)
'''

# example:
df.pivot_table(values='sales', index='region', columns='product', aggfunc='sum')
# output:
# product   A     B
# region
# North    220   150
# South    200   300

'''
# instead of a flat list like groupby gives, you get a matrix — regions as rows, products as columns, sales values inside.
'''

# multiple aggfuncs:
df.pivot_table(values='sales', index='region', aggfunc=['sum', 'mean'])
# output:
#         sum   mean
# region
# North   370   123.3
# South   500   250.0

'''

# fill NaN values (when a combination doesn't exist):
df.pivot_table(values='sales', index='region', columns='product', 
               aggfunc='sum', fill_value=0)

'''

# groupby vs pivot_table:
'''
groupby → flat result (good for one grouping)
pivot_table → matrix result (good for comparing two dimensions)
'''


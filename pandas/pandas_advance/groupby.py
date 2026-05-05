'''starting with groupby.

groupby
Think of it like SQL's GROUP BY — split data into groups, apply a function, get results.
pythonimport pandas as pd'''

import pandas as pd

# groupby example

df = pd.DataFrame({
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi'],
    'sales': [100, 200, 150, 300, 120],
    'product': ['A', 'B', 'A', 'C', 'B']
})

# basic groupby
print(df.groupby('city')['sales'].sum())
# Delhi     370
# Mumbai    500
print()

# multiple aggs at once
print(df.groupby('city')['sales'].agg(['sum', 'mean', 'count']))
print()

# groupby multiple columns
print(df.groupby(['city', 'product'])['sales'].sum())   
print()

# agg function
'''.agg() is the most useful — in interviews you'll almost always need multiple aggregations together.
python# custom agg per column'''


print(df.groupby('city').agg(
    total_sales=('sales', 'sum'),
                #column   #function
    avg_sales=('sales', 'mean'),
    num_orders=('sales', 'count')
))
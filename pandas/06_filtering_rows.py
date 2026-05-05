import pandas as pd

# filtering rows:-
# Getting rows that match a condition — 
# same as NumPy boolean masking but on a DataFrame.

df = pd.read_csv('students.csv')
print(df[df['marks'] > 80]) # rows where marks > 80

# exact match
print(df[df['city'] == 'Delhi'])

# not equal
print(df[df['city'] != 'Delhi'])

# passed students only
print(df[df['passed'] == True])


print()
# multiple conditions: use & (and), | (or) with parentheses:

# students from Delhi who passed
print(df[(df['city'] == 'Delhi') & (df['passed'] == True)])

# students from Delhi or Mumbai 
print(df[(df['city'] == 'Delhi') | (df['city'] == 'Mumbai')])

# isin() — filter multiple values:
print(df[df['city'].isin(['Delhi', 'Pune'])])

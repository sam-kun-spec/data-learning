import pandas as pd

# viewing data:-
# First thing you do after loading any dataset — quickly
# understand what's inside before doing anything else.

#head() & tail():

df = pd.read_csv('students.csv')

print(df.head())    # first 5 rows (default)
print(df.head(3))   # first 3 rows
print(df.tail(2))   # last 2 rows


# info() & describe():
print()

print(df.info())     # summary of the DataFrame
print()
print(df.describe()) # statistical summary of numerical columns


# Real workflow every time you load data:
print()

df = pd.read_csv('students.csv')
df.head()      # see sample
df.info()      # check dtypes + nulls
df.describe()  # check stats
df.shape       # check size, rows & columns

# → these 4 lines = your standard starting point for any DA project.

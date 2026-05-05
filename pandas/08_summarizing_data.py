import pandas as pd
import numpy as np

# summarizing data:- 
# Summarizing and aggregating data — 
# this is where actual insights come from in DA work.

df = pd.read_csv('students.csv')

#sort values:

print(df.sort_values('marks'))  # sort by marks ascending
print()
print(df.sort_values('marks', ascending=False))  # sort by marks descending
print()

# value counts:

print(df.value_counts('city'))  # count of each unique city
print()

# groupby:

print(df.groupby('city')['marks'].mean())  # average marks by city
print()
print(df.groupby('city')['marks'].sum())  # total marks by city
print()

# groupby with aggregation:

print(df.groupby('city').agg({'marks': ['mean', 'sum']}))  # multiple agg funcs
print()

# distribution:
print(df['city'].value_counts())  # distribution of cities
print()

# top 3 students by marks:
print(df.sort_values('marks', ascending=False).head(4).to_string(index=False))  # top 3 by marks, also print without index, to_string converts the DataFrame to a plain string for printing.


"""
Real DA workflow:

df.groupby('city')['marks'].mean()   # avg marks by city
df['city'].value_counts()            # distribution
df.sort_values('marks', ascending=False).head(3)  # top 3

"""


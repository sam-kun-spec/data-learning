import pandas as pd
import numpy as np

# handling missing values:-
# Real datasets always have missing data.
# Before any analysis you need to find and handle them.

df = pd.DataFrame({
    'name': ['Sam', 'Raj', 'Priya', 'Amit', 'Neha'],
    'marks': [85, None, 78, 60, None],
    'city': ['Delhi', 'Mumbai', None, 'Delhi', 'Chennai']
})
print(df) # NaN = Not a Number → represents missing values
 

print()
# let's find missing values:

print(df.isnull()) # print true if value is missing
print()
print(df.isnull().sum()) # count missing values in each column


print()
# drop missing values:-

print(df.dropna()) # drop (not include) rows with any missing values
print()
print(df.dropna(subset=['marks'])) # drop rows where marks is missing


print()
# fill missing values:-

print(df.fillna(0)) # fill all missing values with 0
print()
print(df['marks'].fillna(0)) # fill missing marks with 0
print()
print(df['marks'].fillna(df['marks'].mean())) # fill missing marks with mean of marks
print()
print(df['city'].fillna('Unknown')) # fill missing strings with 'Unknown'


"""
Which to use — drop or fill?
dropna → when missing data is very less (< 5%)
fillna → when you can't afford to lose data.

"""
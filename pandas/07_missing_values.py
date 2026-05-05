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
print(df.isnull().sum().sum()) # total missing values in entire dataframe


print()
# drop missing values:-

print(df.dropna()) # drop (not include) rows with any missing values
print()
print(df.dropna(subset=['marks'])) # drop rows where marks is missing
print()
print(df.dropna(how='all')) # drop rows only if all values are missing


print()
# fill missing values:-

print(df.fillna(0)) # fill all missing values with 0
print()
print(df['marks'].fillna(0)) # fill missing marks with 0
print()
print(df['marks'].fillna(df['marks'].mean())) # fill missing marks with mean of marks
print()
print(df['city'].fillna('Unknown')) # fill missing strings with 'Unknown'
print()
print(df['marks'].ffill()) # forward fill = use previous row value
print()
print(df['marks'].bfill()) # backward fill = use next row value


print()
# ffill vs bfill visual:

salary = pd.Series([50000, np.nan, np.nan, 70000])
print(salary)
print()
print(salary.ffill()) # NaN takes previous value
print()
print(salary.bfill()) # NaN takes next value


"""
Which to use — drop or fill?
dropna → when missing data is very less (< 5%)
fillna → when you can't afford to lose data.


Which fill to use when?
numerical column   → fillna(mean()) or fillna(median())
categorical column → fillna(mode()[0]) or fillna('Unknown')
time series data   → ffill() or bfill()

"""

# Important: `fillna()` does NOT modify the original Series/DataFrame in-place by default.
# You must assign the result back to save changes. Examples:
# df['price'] = df['price'].fillna(df['price'].mean())
# df['category'] = df['category'].fillna('Unknown')
# df['rating'] = df['rating'].fillna(df['rating'].median())

print()
print('Important note: fillna() returns a new object; assign back to persist changes')
print()
# demo showing assignment to save changes:
demo = pd.DataFrame({
    'price': [100, None, 150, None],
    'category': ['A', None, 'B', None],
    'rating': [4.5, None, 3.8, None]
})
print('Before (demo):')
print(demo)

demo['price'] = demo['price'].fillna(demo['price'].mean())
demo['category'] = demo['category'].fillna('Unknown')
demo['rating'] = demo['rating'].fillna(demo['rating'].median())

print()
print('After (demo):')
print(demo)
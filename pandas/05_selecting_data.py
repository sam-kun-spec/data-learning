import pandas as pd

# selecting data:- 
# Grabbing specific rows/columns from your DataFrame.


# columns:
df = pd.read_csv('students.csv')
print(df['name'])  # single column → Series
print()
print(df[['name', 'marks']])  # multiple columns → DataFrame


print()
# rows: we use .loc[] & .iloc[] to select rows :-

# loc[row, column]
print(df.loc[0])            # entire row 0
print(df.loc[0, 'name'])    # row 0, name column
print(df.loc[0:2, 'name':'marks'])  # rows 0 to 2, columns name to marks

print()
# iloc — position based: rows & columns both by numeric index:
print(df.iloc[0])            # entire row 0
print(df.iloc[0, 1])     # row 0, col 1
print(df.iloc[0:2, 0:2]) # slice by position

"""
Simple rule:
loc  → use names  → df.loc[0, 'marks']
iloc → use numbers → df.iloc[0, 1]

"""

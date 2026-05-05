import pandas as pd


# Series :-
# Series = a single column (1D) of data

a = pd.Series([10, 20, 30, 40])
print(a) # → left side = index, right side = values


print()
# dataframe:- 
# dataframe = full (2D) table of data , multiple columns.

b = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

print(b) # → rows + columns, just like Excel

"""
Key difference:
Series    → one column only  → like np.array but with index
DataFrame → multiple columns → like a full Excel sheet

In real DA work:

you'll almost always work with DataFrames
Series comes up when you select one column from a DataFrame

"""
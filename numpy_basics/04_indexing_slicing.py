# indexing and slicing in numpy:- 

# Grabbing specific elements or portions of your array — essential for data work.

import numpy as np

arr = np.array([1,2,3,4])

print(arr[0])   # first element (index starts at 0)
print(arr[1])   # second element
print(arr[-1])  # last element
print(arr[-2])  # second to last element

# Slicing
print(arr[1:3]) # elements from index 1 to 2 (3 is not included)
print(arr[:3])  # elements from the beginning to index 2
print(arr[::2]) # every other element
print(arr[::-1]) # reverse the array

# 2d array 
print()

arr2d = np.array([[1,2,3],
                  [4,5,6], 
                  [7,8,9]])

print(arr2d[0, 1])   # row 0, col 1  #think of it as → arr[row, col]
print(arr2d[2, 2])   # row 2, col 2 

print(arr2d[0:2, 1:3])  # first 2 rows, last 2 cols


# visually to remeber
"""
        col0  col1  col2
row0  →  [1,   2,    3]
row1  →  [4,   5,    6]
row2  →  [7,   8,    9]

arr2d[1, 2] = 6  ✓
"""

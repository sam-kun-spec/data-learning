# Array Properties :-

# Before working with data, you need to know the shape, size, type of your array 
# — like checking a dataset before analyzing it.

import numpy as np

arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

print(arr.shape)   # rows x columns , (2, 3) means 2 rows and 3 columns
print(arr.ndim)    # number of dimensions , 2d array has 2 dimensions
print(arr.size)    # total elements , 2 x 3 = 6
print(arr.dtype)   # data type , default is int64 for integers

#dtype = data type of the elements in the array.
print()

print(np.array([1, 2, 3]).dtype)        # int64 , default for integers, 
print(np.array([1.0, 2.0]).dtype)       # float64 , default for floats
print(np.array([1, 2.0]).dtype)         # float64 , mixed
print(np.array(['a', 'b']).dtype)       # <U1 (string) , U stands for Unicode, 1 means max length of string is 1 character
print(np.array(['hello', 'world']).dtype)       # <U5 (string) ,  U stands for Unicode, 5 means max length of string is 5 characters
print(np.array([True, False]).dtype)   # bool (boolean)

"""
 Note for DA work:
.shape and .dtype are the first things you check when
 debugging data issues — wrong shape or wrong dtype = most common errors.
"""





#reshape and flatten :- 

#Changing the shape of an array without changing its data,
#very common when feeding data into ML models or restructuring datasets.

import numpy as np

arr = np.arange(1, 7)  # [1 2 3 4 5 6]
print(arr)
print(arr.shape)        # (6,) → 1D

# Reshape to 2D
arr2d = arr.reshape(2, 3)  # 2 rows, 3 cols. , total elements must match 2*3 = 6
print(arr2d)
 

# Flatten back to 1D
print()

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.flatten())  # [1 2 3 4 5 6] → flattens to 1D


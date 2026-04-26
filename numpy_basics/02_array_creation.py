import numpy as np

# a numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# multiplication on numpy arrays ( also for addition, subtraction, division )
result = arr * 2
print(result)

# 2d array (matrix)
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d)

print()
# ************* #

print(np.zeros(5))        # array of 5 zeros
print(np.ones(5))         # array of 5 ones
print(np.arange(0,10,2))  # 0 to 9, step 2
print(np.linspace(0,1,5)) # 5 numbers between 0 and 1, equally spaced


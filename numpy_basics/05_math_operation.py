# maths operation:- 

# NumPy lets you do math on entire arrays at once and 
# no loops needed. This is the main reason it's used in data work.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr + 5)   # add 5 to every element
print(arr * 2)   # multiply every element by 2
print(arr - 10)  # subtract
print(arr / 2)   # divide


#Array + Array: → operates element by element
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a+b)
print(a*b)


#built in functions:-
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))    # total
print(np.mean(arr))   # average
print(np.min(arr))    # minimum
print(np.max(arr))    # maximum
print(np.std(arr))    # standard deviation , how spread out the numbers are from the mean. - mean = 30 (average)
#std = 14.14 → numbers are ~14 units away from 30 on average
print(np.sqrt(arr))   # square root 


# 2d array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

print(np.sum(arr2d))
print(np.sum(arr2d, axis=0))  # column-wise sum
print(np.sum(arr2d, axis=1))  # row-wise sum
# Boolean Masking:-

# Filtering data based on a condition — most used feature in real DA
# work. Instead of loops, you just write a condition.

import numpy as np

arr = np.array([10, 15, 20, 25, 30])
print(arr>20) #→ numpy checks each element, returns True/False

print(arr[arr>20]) # give me elements where condition is True , masking the array.

# more conditions:-
print(arr[arr == 30])   # equal to
print(arr[arr != 30])   # not equal to
print(arr[arr <= 25])   # less than or equal

#multiple conditions:-
print(arr[(arr>15) & (arr<30)]) # → numbers greater than 15 and less than 30
print(arr[(arr<15) | (arr>25)]) # → numbers less than 15 or greater than 25


# Real DA use case:-

salaries = np.array([20000, 45000, 60000, 35000, 80000])

# who earns more than 40k?
print(salaries[salaries > 40000])
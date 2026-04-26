# any() returns True if at least one element in the iterable is truthy
# Python any() function returns True if any of the elements of a given iterable( List, Dictionary, Tuple, set, etc) 
# are True else it returns False.

numbers = [0, 0, 0, 5, 0]
print(any(numbers))        # True  — 5 is truthy

empty = []
print(any(empty))          # False — no elements at all

all_false = [0, False, None, ""]
print(any(all_false))      # False — all are falsy

names = ["", "", "Alice"]
print(any(names))          # True  — "Alice" is truthy

# Using any() with a generator expression
scores = [30, 55, 48, 72, 60]
passed = any(score >= 70 for score in scores)
print(passed)              # True  — 72 is >= 70

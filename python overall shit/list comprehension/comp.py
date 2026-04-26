# List Comprehension
# A concise way to create lists in a single line.
# Syntax: [expression for item in iterable if condition]

# Example 1: Squares of numbers 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Example 2: Even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8]

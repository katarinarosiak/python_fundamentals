# Multiplicative Average
# Write a method that takes an Array of integers as input, multiplies all the numbers together, divides the result by the number of entries in the Array, and then prints the result rounded to 3 decimal places. Assume the array is non-empty.

# Examples:

# Copy Code
# show_multiplicative_average([3, 5])                # => The result is 7.500
# show_multiplicative_average([6])                   # => The result is 6.000
# show_multiplicative_average([2, 5, 7, 11, 13, 17]) # => The result is 28361.667
from functools import reduce


def show_multiplicative_average(arr):
    multiplied = reduce(lambda x, y: x * y, arr)
    return format(multiplied / len(arr), ".3f")


# Copy Code
print(show_multiplicative_average([3, 5]))  # => The result is 7.500
print(show_multiplicative_average([6]))  # => The result is 6.000
print(show_multiplicative_average([2, 5, 7, 11, 13, 17]))  # => The result is 28361.667

# Multiply Lists
# Write a method that takes two Array arguments in which each Array contains a list of numbers, and returns a new Array that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

# Examples:


def multiply_list(arr1, arr2):

    multiplied = [num * arr2[arr1.index(num)] for num in arr1]
    return multiplied


# Copy Code
print(multiply_list([3, 5, 7], [9, 10, 11]))  # == [27, 50, 77]

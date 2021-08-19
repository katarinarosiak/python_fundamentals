# Rotation (Part 1)
# Write a method that rotates an array by moving the first element to the end of the array. The original array should not be modified.

# Do not use the method Array#rotate or Array#rotate! for your implementation.

# Example:

# Copy Code
# rotate_array([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7]
# rotate_array(['a', 'b', 'c']) == ['b', 'c', 'a']
# rotate_array(['a']) == ['a']

# x = [1, 2, 3, 4]
# rotate_array(x) == [2, 3, 4, 1]   # => true
# x == [1, 2, 3, 4]                 # => true

# - copy of an array
# -

# -edge cases:
# [] => []
# [a] => [a]
# {}, 0, null => []
# [1,1,1,] => [1,1,1]
# [a, 1, None, 'a'] => [1, None, 'a', a]

# - create an empty array
# - slice first char,
# - slice the rest
# - place the rest in an array
# - place the first char in the end
# - return the array


def rotate_array(arr):
    if not isinstance(arr, list) or not len(arr):
        return []

    return arr[1 : len(arr)] + arr[0:1]


print(rotate_array([7, 3, 5, 2, 9, 1]))

print(rotate_array([7, 3, 5, 2, 9, 1]))  # == [3, 5, 2, 9, 1, 7]
print(rotate_array(["a", "b", "c"]))  # == ['b', 'c', 'a']
print(rotate_array(["a"]))  # == ['a']

# Counting Up
# Write a method that takes an integer argument, and returns an Array of all integers, in sequence, between 1 and the argument.

# You may assume that the argument will always be a valid integer that is greater than 0.

# Examples:

# Copy Code
# sequence(5) == [1, 2, 3, 4, 5]
# sequence(3) == [1, 2, 3]
# sequence(1) == [1]


def sequence(num):
    return [i for i in range(1, num + 1)]


print(sequence(5) == [1, 2, 3, 4, 5])
print(sequence(3) == [1, 2, 3])
print(sequence(1) == [1])

# Sum of Sums
# Write a method that takes an Array of numbers and then returns the sum of the sums of each leading subsequence for that Array. You may assume that the Array always contains at least one number.


def sum_of_sums(arr):
    index = 1
    final = []
    for num in arr:
        final.append(sum(arr[0:index:1]))
        index += 1

    return sum(final)


# Examples:

# Copy Code
print(sum_of_sums([3, 5, 2]))  # == (3) + (3 + 5) + (3 + 5 + 2) # -> (21)
print(
    sum_of_sums([1, 5, 7, 3])
)  # == (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) # -> (36)
print(sum_of_sums([4]))  # == 4
print(sum_of_sums([1, 2, 3, 4, 5]))  # == 35

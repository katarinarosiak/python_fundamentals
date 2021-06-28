# Halvsies
# Write a method that takes an Array as an argument, and returns two Arrays (as a pair of nested Arrays) that contain the first half and second half of the original Array, respectively. If the original array contains an odd number of elements, the middle element should be placed in the first half Array.


def halvsies(arr):
    final = []
    if len(arr) % 2 == 0:
        half = int((len(arr)) / 2)
        return [arr[:half], arr[half:]]
    else:
        half = int(((len(arr)) + 1) / 2)
        return [arr[:half], arr[half:]]


# Examples:

# Copy Code
print(halvsies([1, 2, 3, 4]))  # == [[1, 2], [3, 4]]
print(halvsies([1, 5, 2, 4, 3]))  # == [[1, 5, 2], [4, 3]]
print(halvsies([5]))  # == [[5], []]
print(halvsies([]))  # == [[], []]

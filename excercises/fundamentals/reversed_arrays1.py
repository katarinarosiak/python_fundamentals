# Reversed Arrays (Part 1)
# Write a method that takes an Array as an argument, and reverses its elements in place; that is, mutate the Array passed into this method. The return value should be the same Array object.

# You may not use Array#reverse or Array#reverse!.

# Examples:

# Copy Code
# list = [1,2,3,4] 1,2,3,4,
# result = reverse!(list)
# result == [4, 3, 2, 1] # true
# list == [4, 3, 2, 1] # true
# list.object_id == result.object_id # true

# list = %w(a b e d c)
# reverse!(list) == ["c", "d", "e", "b", "a"] # true
# list == ["c", "d", "e", "b", "a"] # true

# list = ['abc']
# reverse!(list) == ["abc"] # true
# list == ["abc"] # true

# list = []
# reverse!(list) == [] # true
# list == [] # true
# Note: for the test case list = ['abc'], we want to reverse the elements in the array. The array only has one element, a String, but we're not reversing the String itself, so the reverse! method call should return ['abc'].

# - extract a slice from teh given array
# - take the last el from the slice
# - clear arr
# -  push the ;ast el of the slice to the list
# - continue until the end of the slice


def reverse_list(list_to_reverse):
    slice = list_to_reverse[::]
    list_to_reverse.clear()

    while len(slice) > 0:
        list_to_reverse.append(slice[-1])
        slice.pop()

    return list_to_reverse


print(reverse_list([1, 2, 3]))
print(reverse_list(["a", "b", "e", "d", "c"]))
print(reverse_list(["abc"]))

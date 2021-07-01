# Does My List Include This?
# Write a method named include? that takes an Array and a search value as arguments. This method should return true if the search value is in the array, false if it is not. You may not use the Array#include? method in your solution.


def include(arr, val):

    for num in arr:
        if val == num:
            return True
    return False


# Copy Code
print(include([1, 2, 3, 4, 5], 3))  # == true
print(include([1, 2, 3, 4, 5], 6))  # == false
print(include([], 3))  # == false
print(include([None], None))  # == true
print(include([], None))  # == false

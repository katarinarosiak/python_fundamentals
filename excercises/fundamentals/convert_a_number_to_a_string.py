# Convert a Number to a String!
# In the previous two exercises, you developed methods that convert simple numeric strings to signed Integers. In this exercise and the next, you're going to reverse those methods.

# Write a method that takes a positive integer or zero, and converts it to a string representation.

# You may not use any of the standard conversion methods available in Ruby, such as Integer#to_s, String(), Kernel#format, etc. Your method should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

# #Examples

# - previous  [1]  minus the last el
# continue until the result no == the result before
# 1. [4000, 300, 20, 1]
#   - num % 1
# 2. reverse the list
# - 1, check in lib and the string push to new arr   ['1']
# 2. 4000 / 1000 and then check in the lib
# 3.  reverse, join array return


# iterete the lib
# - extract the last num and compare if same psuh to new arr the index


def integer_to_string(num):
    lib = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numerals = []
    divider = 10
    integers = []
    final_str = ""

    while True:
        current = num % divider
        numerals.append(current)
        divider = divider * 10

        if current == num:
            break

    divider = 1
    for i in numerals:
        integers.append(int(i / divider))
        divider *= 10

    integers.reverse()

    for i in integers:
        final_str += lib[i]
    return final_str


print(integer_to_string(4321))


print(integer_to_string(4321) == "4321")
print(integer_to_string(0) == "0")
print(integer_to_string(5000) == "5000")

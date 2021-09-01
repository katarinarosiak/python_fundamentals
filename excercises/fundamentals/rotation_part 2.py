# Rotation (Part 2)
# Write a method that can rotate the last n digits of a number. For example:

# Copy Code
# rotate_rightmost_digits(735291, 1) == 735291
# rotate_rightmost_digits(735291, 2) == 735219
# rotate_rightmost_digits(735291, 3) == 735912
# rotate_rightmost_digits(735291, 4) == 732915
# rotate_rightmost_digits(735291, 5) == 752913
# rotate_rightmost_digits(735291, 6) == 352917
# Note that rotating just 1 digit results in the original number being returned.

# You may use the rotate_array method from the previous exercise if you want. (Recommended!)

# You may assume that n is always a positive integer.

# i: number, number
# o: number

# goal: extract part of the number of a length as the second argument and rotate them. join them with the remaining part and return.

# rules:
# explicit:
# - n is always positive and a number
# - we rotate the last n digitis of a number
# - if n is 1 we return the number

# implicit:
# - we always get two arguments
# -

# 1. extract part of a digiti to rotate (n digitis)
#   - coerce to string
#   - cut a slice of a string of n length
# from the end
#     - start cut from length - n
#     - end cut at length - 1


# 2. Rotate a digit
#   - cut first character
#   - cut all the remaining part of the string without first character
#   - concattinete longest part of a string with the shortest
#   - return


# return rotateted number


def rotate(char_str):
    return char_str[1::] + char_str[0:1]


def rotate_rightmost_digits(num, digits):
    coerced_to_str = str(num)
    sliced_start = coerced_to_str[0 : len(coerced_to_str) - digits]
    sliced_end = coerced_to_str[len(coerced_to_str) - digits : len(coerced_to_str)]

    rotated = rotate(sliced_end)

    return int(sliced_start + rotated)


print(rotate_rightmost_digits(735291, 2) == 735219)
print(rotate_rightmost_digits(735291, 1) == 735291)
print(rotate_rightmost_digits(735291, 3) == 735912)
print(rotate_rightmost_digits(735291, 4) == 732915)
print(rotate_rightmost_digits(735291, 5) == 752913)
print(rotate_rightmost_digits(735291, 6) == 352917)

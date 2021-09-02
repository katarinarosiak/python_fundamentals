# # Rotation (Part 3)
# # If you take a number like 735291, and rotate it to the left, you get 352917. If you now keep the first digit fixed in place, and rotate the remaining digits, you get 329175. Keep the first 2 digits fixed in place and rotate again to 321759. Keep the first 3 digits fixed in place and rotate again to get 321597. Finally, keep the first 4 digits fixed in place and rotate the final 2 digits to get 321579. The resulting number is called the maximum rotation of the original number.

# # Write a method that takes an integer as argument, and returns the maximum rotation of that argument. You can (and probably should) use the rotate_rightmost_digits method from the previous exercise.

# # Note that you do not have to handle multiple 0s.

# # Example:

# # Copy Code
# # max_rotation(735291) == 321579
# # max_rotation(3) == 3
# # max_rotation(35) == 53
# # max_rotation(105) == 15 # the leading zero gets dropped
# # max_rotation(8_703_529_146) == 7_321_609_845

# i: int
# o: int (max rotation number)


# - take a number and rotate it to the left
# - leave first digit and rotate the rest
# - leave second digit and rotate the rest
# - continue until two last digits are rotatetd

# - take a digit and coerce it to a string
# - rotate the number length - 1 times, decrementing number of digits to rotate from the end (by one)
#     -take the string and slice it starting from the start number until the end
#     - save the remaining part in variable
#     - the ending part rotate and concatenate with the remaining part
#     - return
# - coerce it back to a digit and return


def rotate(char_str, digits):
    start = len(char_str) - digits
    remaining = char_str[0:start]
    sliced = char_str[start : len(char_str)]
    rotated = sliced[1 : len(sliced)] + sliced[0]
    return remaining + rotated


def max_rotation(digit):
    char_str = str(digit)
    idx = len(char_str)
    rotatetd = char_str

    for char in range(len(char_str) - 1):
        rotatetd = rotate(rotatetd, idx)
        idx -= 1

    return int(rotatetd)


print(max_rotation(735291) == 321579)
print(max_rotation(3) == 3)
print(max_rotation(35) == 53)
print(max_rotation(105) == 15)  # the leading zero gets dropped
print(max_rotation(8_703_529_146) == 7_321_609_845)

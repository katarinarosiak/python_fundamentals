# Always Return Negative
# Write a method that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the number is 0 or negative, return the original number.

# Examples:

# Copy Code
# negative(5) == -5
# negative(-3) == -3
# negative(0) == 0      # There's no such thing as -0 in ruby


def negative(num):
    if num > 0:
        return num * -1
    else:
        return num


print(negative(5) == -5)
print(negative(-3) == -3)
print(negative(0) == 0)  # There's no such thing as -0 in ruby

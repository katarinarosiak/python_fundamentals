# Diamonds!
# Write a method that displays a 4-pointed diamond in an n x n grid, where n is an odd integer that is supplied as an argument to the method. You may assume that the argument will always be an odd integer.

# PEDAC
# count break
# count diamonds
# iterate top
# iterate bottom
# ceil 9/2
# num -  ceil(9/2)

# - count the numbers of iteration for the top part
#   - input number devide by two and round up. save the number to a variable
#   - iterate and on eahc iteratuion
#   - count the breaks
#     - num /2 and round down
#   - count the diamonds
#     - start with one

#   - incement diamond by 1
#   - decrement break by 1
# count the number of iteration for the bottom part
#  - input number  devide by two and round down
#  - print
#  - iterate
#  - take the break num and diamonds num
#  - decrement diamonds and increment breaks on every iteration
#  print

# Examples

# Copy Code
# diamond(1)

# *
# Copy Code
# diamond(3)

#  *
# ***
#  *
# Copy Code
# diamond(9)

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
import math


def diamond(size):
    breaks = round(size / 2)
    diamonds = 1

    for i in range(size):
        print(" " * breaks + "*" * diamonds + " " * breaks)

        if i < math.floor(size / 2):
            breaks -= 1
            diamonds += 2
        else:
            breaks += 1
            diamonds -= 2


diamond(3)

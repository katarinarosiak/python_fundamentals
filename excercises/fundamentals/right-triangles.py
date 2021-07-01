# Write a method that takes a positive integer, n, as an argument, and displays a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

# 4b 1s
# 3b 2s
# 2b 3s
# 1b 4s
# 0b 5s


def triangle(num):
    breaks = num - 1
    stars = 1
    star = "*"
    space = " "

    while stars <= num:

        print(space * breaks, star * stars)
        breaks -= 1
        stars += 1


# Examples:

triangle(5)

#     *
#    **
#   ***
#  ****
# *****

triangle(9)

#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

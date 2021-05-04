# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer greater than 0, then asks if the user wants to determine the sum or product of all numbers between 1 and the entered integer.

# Examples:
# >> Please enter an integer greater than 0:
# 5
# >> Enter 's' to compute the sum, 'p' to compute the product.
# s
# The sum of the integers between 1 and 5 is 15.


# >> Please enter an integer greater than 0:
# 6
# >> Enter 's' to compute the sum, 'p' to compute the product.
# p
# The product of the integers between 1 and 6 is 720.
from functools import reduce

user_integer = int(input("Please enter an integer greater than 0: "))
sum_or_product = input("Enter 's' to compute the sum, 'p' to compute the product: ")
numbers = [*range(1, user_integer + 1)]
result = 1

if sum_or_product == "s":
    result = sum(numbers)
    print(numbers)
    print(f"The sum of the integers between 1 and {user_integer} is {result}")
elif sum_or_product == "p":
    for num in numbers:
        result = result * num
        print(numbers)
        print(f"The product of the integers between 1 and {user_integer} is {result}")
else:
    print("The input is incorrect")

# Arithmetic Integer
# Write a program that prompts the user for two positive integers, and then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, remainder, and power. Do not worry about validating the input.

# Example

# Copy Code
# ==> Enter the first number:
# 23
# ==> Enter the second number:
# 17
# ==> 23 + 17 = 40
# ==> 23 - 17 = 6
# ==> 23 * 17 = 391
# ==> 23 / 17 = 1
# ==> 23 % 17 = 6
# ==> 23 ** 17 = 141050039560662968926103

first = input("Enter the first number: ")
second = input("Enter the second number: ")
operations = ("+", "-", "*", "/", "%", "**")

for op in operations:
    result = eval(f"{first} {op} {second}")
    print(f"==> {first} {op} {second} = {result}")

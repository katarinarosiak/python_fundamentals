# Palindromic Numbers
# Write a method that returns true if its integer argument is palindromic, false otherwise. A palindromic number reads the same forwards and backwards.


def palindromic_number(num):
    return str(num)[::-1] == str(num)


print(palindromic_number(34543) == True)
print(palindromic_number(123210) == False)
print(palindromic_number(22) == True)
print(palindromic_number(5) == True)

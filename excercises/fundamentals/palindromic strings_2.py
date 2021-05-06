# Palindromic Strings (Part 2)
# Write another method that returns true if the string passed as an argument is a palindrome, false otherwise. This time, however, your method should be case-insensitive, and it should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the palindrome? method you wrote in the previous exercise.
import re


def is_palindrome(str):
    return str[::-1].lower() == str.lower()


def real_palindrome(str):
    str = re.sub("[^0-9a-zA-Z]+", "", str)
    return is_palindrome(str)


print(real_palindrome("123 abc 123"))

print(real_palindrome("madam") == True)
print(real_palindrome("Madam") == True)  # (case does not matter)
print(real_palindrome("Madam, I'm Adam") == True)  # (only alphanumerics matter)
print(real_palindrome("356653") == True)
print(real_palindrome("356a653") == True)
print(real_palindrome("123ab321") == False)

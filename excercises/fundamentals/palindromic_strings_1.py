# Palindromic Strings (Part 1)
# Write a method that returns true if the string passed as an argument is a palindrome, false otherwise. A palindrome reads the same forward and backward. For this exercise, case matters as does punctuation and spaces.
def is_palindrome(word):
    return word[::-1] == word


print(is_palindrome("madam"))  # == true
print(is_palindrome("Madam"))  # == false          # (case matters)
print(is_palindrome("madam i'm adam"))  # == false # (all characters matter)
print(is_palindrome("356653"))  # == true

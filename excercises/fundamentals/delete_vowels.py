# Delete vowels
# Write a method that takes an array of strings, and returns an array of the same string values, except with the vowels (a, e, i, o, u) removed.

# Example:

# Copy Code
# remove_vowels(%w(abcdefghijklmnopqrstuvwxyz)) == %w(bcdfghjklmnpqrstvwxyz)
# remove_vowels(%w(green YELLOW black white)) == %w(grn YLLW blck wht)
# remove_vowels(%w(ABC AEIOU XYZ)) == ['BC', '', 'XYZ']
import re


def remove_vowels(words):
    arrOfWords = []
    for word in words:
        arrOfWords.append(re.sub("[aeiou]", "", word, flags=re.IGNORECASE))

    return arrOfWords


# Copy Code
print(remove_vowels(["abcdefghijklmnopqrstuvwxyz"]))  # == %w(bcdfghjklmnpqrstvwxyz)
print(remove_vowels(["green", "YELLOW", "black", "white"]))  # == %w(grn YLLW blck wht)
print(remove_vowels(["ABC", "AEIOU", "XYZ"]))  # == ['BC', '', 'XYZ']

# Lettercase Counter
# Write a method that takes a string, and then returns a hash that contains 3 entries: one represents the number of characters in the string that are lowercase letters, one the number of characters that are uppercase letters, and one the number of characters that are neither.
import string


def is_letter(letter):
    alpha = list(string.ascii_lowercase + string.ascii_uppercase)
    return letter in alpha


def letter_case_count(str_of_letters):
    counted_letters = {"lowercase": 0, "uppercase": 0, "neither": 0}

    for letter in list(str_of_letters):
        if letter.upper() == letter and is_letter(letter):
            counted_letters["uppercase"] += 1
        elif letter.lower() == letter and is_letter(letter):
            counted_letters["lowercase"] += 1
        else:
            counted_letters["neither"] += 1

    return counted_letters


# Examples

# Copy Code
print(letter_case_count("abCdef 123"))  # == { lowercase: 5, uppercase: 1, neither: 4 }
print(letter_case_count("AbCd +Ef"))  # == { lowercase: 3, uppercase: 3, neither: 2 }
print(letter_case_count("123"))  # == { lowercase: 0, uppercase: 0, neither: 3 }
print(letter_case_count(""))  # == { lowercase: 0, uppercase: 0, neither: 0 }

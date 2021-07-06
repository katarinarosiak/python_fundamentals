# Swap Case
# Write a method that takes a string as an argument and returns a new string in which every uppercase letter is replaced by its lowercase version, and every lowercase letter by its uppercase version. All other characters should be unchanged.

# You may not use String#swapcase; write your own version of this method.


def swapcase(sentence):
    swaped = ""

    for char in sentence:
        if char.upper() == char:
            swaped += char.lower()
        else:
            swaped += char.upper()
    return swaped


# Example:

# Copy Code
print(swapcase("CamelCase"))  # == 'cAMELcASE'
print(swapcase("Tonight on XYZ-TV"))  # == 'tONIGHT ON xyz-tv'

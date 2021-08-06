# Uppercase Check
# Write a method that takes a string argument, and returns true if all of the alphabetic characters inside the string are uppercase, false otherwise. Characters that are not alphabetic should be ignored.

# Examples:

# Copy Code
# uppercase?('t') == false
# uppercase?('T') == true
# uppercase?('Four Score') == false
# uppercase?('FOUR SCORE') == true
# uppercase?('4SCORE!') == true
# uppercase?('') == true


def uppercase(str_arg):
    for char in str_arg:
        if char.upper() != char:
            return False
    return True


print(uppercase("T"))  # == true
print(uppercase("Four Score"))  # == false
print(uppercase("FOUR SCORE"))  # == true
print(uppercase("t"))  # == false
print(uppercase("4SCORE!"))  # == true
print(uppercase(""))  # == true

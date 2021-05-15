# Convert a String to a Signed Number!
# In the previous exercise, you developed a method that converts simple numeric strings to Integers. In this exercise, you're going to extend that method to work with signed numbers.

# Write a method that takes a String of digits, and returns the appropriate number as an integer. The String may have a leading + or - sign; if the first character is a +, your method should return a positive number; if it is a -, your method should return a negative number. If no sign is given, you should return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion methods available in Ruby, such as String#to_i, Integer(), etc. You may, however, use the string_to_integer method from the previous lesson.

# Examples
def string_to_integer(str):
    lib = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    char = list(str)
    num = [lib[i] for i in char]
    final = 0
    multiplier = 1
    num.reverse()

    for i in num:
        final += i * multiplier
        multiplier *= 10
    return final


def string_to_signed_integer(str):
    sign = ""
    if str[0] == "-" or str[0] == "+":
        sign = str[0]
        str = str[1:]
    number = string_to_integer(str)

    if sign == "-":
        return number * -1
    else:
        return number


print(string_to_signed_integer("-4321"))
print(string_to_signed_integer("-570"))  # == -570
print(string_to_signed_integer("+100"))  # == 100

# Get The Middle Character
# Write a method that takes a non-empty string argument, and returns the middle character or characters of the argument. If the argument has an odd length, you should return exactly one character. If the argument has an even length, you should return exactly two characters.

# Examples:

# Copy Code
# center_of('I love ruby') == 'e'
# center_of('Launch School') == ' '
# center_of('Launch') == 'un'
# center_of('Launchschool') == 'hs'
# center_of('x') == 'x'


def center_of(str_arg):
    len_of_str = len(str_arg)
    start = int(len_of_str / 2)
    if len_of_str % 2 == 0:
        return str_arg[start - 1 : start + 1]
    else:
        return str_arg[start : start + 1]


print(center_of("I love ruby") == "e")
print(center_of("Launch School") == " ")
print(center_of("Launch") == "un")
print(center_of("Launchschool") == "hs")
print(center_of("x") == "x")

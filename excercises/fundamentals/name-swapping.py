# Name Swapping
# Write a method that takes a first name, a space, and a last name passed as a single String argument, and returns a string that contains the last name, a comma, a space, and the first name.

# Examples

# Copy Code
# swap_name('Joe Roberts') == 'Roberts, Joe'


def swap_name(name):
    splited_name = name.split(" ")

    return f"{splited_name[1]}, {splited_name[0]}"


print(swap_name("Joe Roberts") == "Roberts, Joe")

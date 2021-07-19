# Leading Substrings
# Write a method that returns a list of all substrings of a string that start at the beginning of the original string. The return value should be arranged in order from shortest to longest substring.


def leading_substrings(some_str):
    arr = [some_str[0 : idx + 1] for idx, char in enumerate(some_str)]
    return arr


# Examples:

# Copy Code
print(leading_substrings("abc"))  # == ['a', 'ab', 'abc']
print(leading_substrings("a"))  # == ['a']
print(leading_substrings("xyzzy"))  # == ['x', 'xy', 'xyz', 'xyzz', 'xyzzy']

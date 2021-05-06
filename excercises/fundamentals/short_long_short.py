# Short Long Short
# Write a method that takes two strings as arguments, determines the longest of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.


def short_long_short(str1, str2):
    if len(str1) > len(str2):
        return str2 + str1 + str2
    else:
        return str1 + str2 + str1


print(short_long_short("abc", "defgh") == "abcdefghabc")
print(short_long_short("abcde", "fgh") == "fghabcdefgh")
print(short_long_short("", "xyz") == "xyz")

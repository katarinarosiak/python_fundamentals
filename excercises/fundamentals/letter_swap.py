# Letter Swap
# Given a string of words separated by spaces, write a method that takes this string of words and returns a string in which the first and last letters of every word are swapped.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces

# - separet a string into a list of word
# - iterate throuch each word and separet each word into list of characters
# - assign first word to a var and second word to another var
# - reassign first and the last letter
# - join
# - join with spaces
# - return


def swap(str):
    words = str.split(" ")
    final = []

    for word in words:
        word = list(word)
        first = word[0]
        last = word[-1]
        word[0] = last
        word[-1] = first
        final.append("".join(word))

    return " ".join(final)


# Examples:

# Copy Code
print(swap("Oh what a wonderful day it is") == "hO thaw a londerfuw yad ti si")
print(swap("Abcde") == "ebcdA")
print(swap("a") == "a")

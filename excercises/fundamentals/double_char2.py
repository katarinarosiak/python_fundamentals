# Double Char (Part 2)
# Write a method that takes a string, and returns a new string in which every consonant character is doubled. Vowels (a,e,i,o,u), digits, punctuation, and whitespace should not be doubled.

# Examples:

# Copy Code
# double_consonants('String') == "SSttrrinngg"
# double_consonants("Hello-World!") == "HHellllo-WWorrlldd!"
# double_consonants("July 4th") == "JJullyy 4tthh"
# double_consonants('') == ""


def double_consonants(word):

    consonants = set("bcdfghjklmnprstvwxyz")

    double_cons = [
        char + char if char in consonants or char.lower() in consonants else char
        for char in word
    ]
    print("".join(double_cons))
    return "".join(double_cons)


print(double_consonants("String") == "SSttrrinngg")
print(double_consonants("Hello-World!") == "HHellllo-WWorrlldd!")
print(double_consonants("July 4th") == "JJullyy 4tthh")
print(double_consonants("") == "")

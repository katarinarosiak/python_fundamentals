# Double Char (Part 1)
# Write a method that takes a string, and returns a new string in which every character is doubled.

# Examples:

# Copy Code
# repeater('Hello') == "HHeelllloo"
# repeater("Good job!") == "GGoooodd  jjoobb!!"
# repeater('') == ''


def repeater(word):
    repeated_word = ""

    for char in word:
        repeated_word += char + char

    print(repeated_word)
    return repeated_word


print(repeater("Hello") == "HHeelllloo")
print(repeater("Good job!") == "GGoooodd  jjoobb!!")
print(repeater("") == "")

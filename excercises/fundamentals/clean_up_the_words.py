# Clean up the words
# Given a string that consists of some words (all lowercased) and an assortment of non-alphabetic characters, write a method that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (the result should never have consecutive spaces).

# rules:
# - no consecutive spaces
# - replace all non-alphabetic with a space

# -iterate throght string
# - check if a space
# - if yes  check if previous character is a space
#   - if it is replace concat ''
#   - else  ' '


def cleanup(str):
    cleaned_str = ""

    for char in str:
        if char.lower() >= "a" and char <= "z":
            cleaned_str += char
        elif len(cleaned_str) > 0:
            if cleaned_str[-1] != " ":
                cleaned_str += " "
        else:
            cleaned_str += " "
    return cleaned_str


# Examples:

# Copy Code
print(cleanup("---what's my +*& line?") == " what s my line ")

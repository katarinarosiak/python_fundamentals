# Staggered Caps (Part 1)
# Write a method that takes a String as an argument, and returns a new String that contains the original value using a staggered capitalization scheme in which every other character is capitalized, and the remaining characters are lowercase. Characters that are not letters should not be changed, but count as characters when switching between upper and lowercase.


def staggered_case(sentence):
    final = ""
    index = 1

    for char in sentence:
        if index % 2 == 0:
            final += char.lower()
        else:
            final += char.upper()
        index += 1

    return final


# Example:

# Copy Code
print(staggered_case("I Love Launch School!"))  # == 'I LoVe lAuNcH ScHoOl!'
print(staggered_case("ALL_CAPS"))  # == 'AlL_CaPs'
print(staggered_case("ignore 77 the 444 numbers"))  # == 'IgNoRe 77 ThE 444 NuMbErS'

# Staggered Caps (Part 2)
# Modify the method from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

# Example:


def staggered_case(sentence):
    counter = 1
    final = ""

    for char in sentence:
        if char.lower() >= "a" and char.lower() <= "z":
            if counter % 2 != 0:
                final += char.upper()
            else:
                final += char.lower()
            counter += 1
        else:
            final += char

    return final


# Copy Code
print(staggered_case("I Love Launch School!"))  # == 'I lOvE lAuNcH sChOoL!'
print(staggered_case("ALL CAPS"))  # == 'AlL cApS'
print(staggered_case("ignore 77 the 444 numbers"))  # == 'IgNoRe 77 ThE 444 nUmBeRs'

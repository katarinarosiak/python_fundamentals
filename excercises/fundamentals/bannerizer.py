# Bannerizer
# Write a method that will take a short line of text, and print it within a box.

# Example:

# Copy Code
# print_in_box('To boldly go where no one has gone before.')
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Copy Code
# print_in_box('')
# +--+
# |  |
# |  |
# |  |
# +--+
# You may assume that the input will always fit in your terminal window.


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1.
# //2.
# //3.
# //Input:
# //- string
# //Output:
# //- print statemnt (string)
# //RULES:
# // Explicit:
# //- the input will always fit in your terminal window.
# //-
# //-
# //-
# //-Implicit
# //- if the input is empty string banner will be ampty (3/3 spaces)
# //- Frame: one spce on eahc side
#    width = lengths of the string + 2 / height 3
# // EDGE CASES:
# // =>
# // =>
# // =>
# //QUESTIONS:
# //- can mutate the obj or need to return new one?
# //- other questions, clarification
# //
# // ------------------------- EXAMPLES/TEST CASES: -------------------
# //input:
# //=>
# //=>
# //=>
# //output:
# //=>
# //=>
# //=>
# // --------------- DIFFERENT SOLUTIONS --------------------------------
# //MENTAL MODEL:
# //*
# //DATA STRUCTURES:
# // ------------------------  ALGORYTHM:  -----------------------------
# //- calculate length of the sentence and save it in a variable
# //- declare five print statement that will take a f string
# //- witihn the f string we will repeat the space or - as may times as the length of the string. surround it with the specific character | , +
# //-
# //-
# //-
# //-
# //-
# //-
# //  ---------------------  PSEUDOCODE:  ------------------------------
# //
# //
# //
# //
# //
# //
# //
# // -------------------------------- CODE:  -----------------------------


def print_in_box(sentence):
    lenOfSentence = len(sentence)

    print(f"+-{'-' * lenOfSentence}-+")
    print(f"| {' ' * lenOfSentence} |")
    print(f"| {sentence} |")
    print(f"| {' ' * lenOfSentence} |")
    print(f"+-{'-' * lenOfSentence}-+")


# Copy Code
print_in_box("To boldly go where no one has gone before.")
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Copy Code
print_in_box("")
# +--+
# |  |
# |  |
# |  |
# +--+

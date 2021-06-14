# ddaaiillyy ddoouubbllee
# Write a method that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

# Examples:

# Copy Code
# crunch('ddaaiillyy ddoouubbllee') == 'daily double'
# crunch('4444abcabccba') == '4abcabcba'
# crunch('ggggggggggggggg') == 'g'
# crunch('a') == 'a'
# crunch('') == ''


# aabb => ab
# aaa => a
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
# //- string
# //RULES:
# // Explicit:
# //- collapse all consecutive duplicates
# //-
# //-
# //-
# //-Implicit
# //- doesn't matter how many characters as long as they are consecutive
# collaps to one
# //- if input is empty str return ampty str
# treat spaces as any other charc, punctuations, numbers as well
# if input is only one letter return that letter
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
# //DATA STRUCTURES: str
# // ------------------------  ALGORYTHM:  -----------------------------
# //- declare empty str
# //- iterate through input str
#       - if it's len == 0 or the last char is not the same
#       - concat
# //- otehrwise continue
# //- return newly created string
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


def crunch(sentence):
    crenched_char = ""

    for char in sentence:
        if len(crenched_char) == 0 or crenched_char[-1] != char:
            crenched_char += char

    return crenched_char


# Examples:

# Copy Code
print(crunch("ddaaiillyy ddoouubbllee"))  # == "daily double"
print(crunch("4444abcabccba"))  # == '4abcabcba'
print(crunch("ggggggggggggggg"))  # == 'g'
print(crunch("a"))  # == 'a'
print(crunch("")) == ""

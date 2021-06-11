# Letter Counter (Part 2)
# Modify the word_sizes method from the previous exercise to exclude non-letters when determining word size. For instance, the length of "it's" is 3, not 4.

# Examples

# Copy Code
# word_sizes('Four score and seven.') == { 3 => 1, 4 => 1, 5 => 2 }
# word_sizes('Hey diddle diddle, the cat and the fiddle!') == { 3 => 5, 6 => 3 }
# word_sizes("What's up doc?") == { 5 => 1, 2 => 1, 3 => 1 }
# word_sizes('') == {}


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
# //- dictionary
# //RULES:
# // Explicit:
# //- count all the word's length
# //- non-alphabetic characters are not counted in the length
# //- return  a dictionary with a count of  how many word have certain length
# //- {len, words count }
# //-Implicit
# //- if input is ampty string returns ampty dictionary
# //-
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
# //DATA STRUCTURES: dictionary, string, array
# // ------------------------  ALGORYTHM:  -----------------------------
# //- declare an empty dictioanry
# //- split a string into a list of words (by space)
#   - declare a counter var
# //- iterate through the list
# //- on each iteration iterate though word
# //-    for each character check if it's a alphabetic
# //-    if it is incemrent counter
# //-     if it's not continue
# //-     check if the dictionary contains a key that ois the same as          #        the counter
# //-     if it's exist incrmeent the value
#         if it doesn't exist create a key and assign a value of 1
#     after iteration is done return the dictionary
# //  ---------------------  PSEUDOCODE:  ------------------------------
# //
# //
# //
# //
# //
# //
# //
# // -------------------------------- CODE:  -----------------------------


def word_sizes(sentence):
    all_words_counted = {}

    if sentence == "":
        return all_words_counted

    words = sentence.split(" ")

    for word in words:
        counter = 0
        for char in word:
            if char.lower() >= "a" and char.lower() <= "z":
                counter += 1
        add_counted(counter, all_words_counted)

    return all_words_counted


def add_counted(counter, all_words_counted):

    if counter in all_words_counted:
        all_words_counted[counter] += 1
    else:
        all_words_counted[counter] = 1


# Copy Code
print(word_sizes("Four score and seven."))  # == { 3 => 1, 4 => 1, 5 => 2 }
print(word_sizes("Hey diddle diddle, the cat and the fiddle!"))  # == { 3 => 5, 6 => 3 }
print(word_sizes("What's up doc?"))  # == { 5 => 1, 2 => 1, 3 => 1 }
print(word_sizes(""))  # == {}

# Letter Counter (Part 1)
# Write a method that takes a string with one or more space separated words and returns a hash that shows the number of words of different sizes.

# Words consist of any string of characters that do not include a space.

# Examples

# Copy Code
# word_sizes('Four score and seven.') == { 3 => 1, 4 => 1, 5 => 1, 6 => 1 }
# word_sizes('Hey diddle diddle, the cat and the fiddle!') == { 3 => 5, 6 => 1, 7 => 2 }
# word_sizes("What's up doc?") == { 6 => 1, 2 => 1, 4 => 1 }
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
# //- method/function
# //- string has at least one word, they are separated by a space
# //- return dictionary with num of word of different sizes
# //- (num of characters => num of words)
# //-Implicit
# //- punctuation is countend as characters , numbers as well
# //- if emoty string return empty dictionary
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
# //DATA STRUCTURES: dictionary, list, string
# // ------------------------  ALGORYTHM:  -----------------------------
# //- declare an empty dictionary
# //- separate words from the string by spaces into a list of words
# //- iterate through that list
# //- count the length of the current word
# //- check if there is a property in the dictionary with that length as a key
# //- if it exist I will increment the value by one
# //- if it doesn't exist assign a key with the length and 1 as a value
# //- continue until the end of the list
# //- return the dictionary
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
    counted_words = {}

    if len(sentence) == 0:
        return counted_words

    words = sentence.split(" ")
    for word in words:
        current_word = str(len(word))

        if current_word in counted_words:
            counted_words[current_word] += 1
        else:
            counted_words[current_word] = 1

    return counted_words


# Copy Code
print(word_sizes("Four score and seven."))  # == { 3 => 1, 4 => 1, 5 => 1, 6 => 1 }
print(
    word_sizes("Hey diddle diddle, the cat and the fiddle!")
)  # == { 3 => 5, 6 => 1, 7 => 2 }
print(word_sizes("What's up doc?"))  # == { 6 => 1, 2 => 1, 4 => 1 }
print(word_sizes(""))  # == {}

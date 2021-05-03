# Write a method that takes a string with one or more space separated words and returns a dictionary that shows the number of words of different sizes.

# Words consist of any string of characters that do not include a space.

# Examples
# input : string
# ourput: dictionary

# if input is an empty string return empty dictionary
# - separate string into array of words
# - remove all other characters than letters:
#    - iterate throgh each word and check if the last char is letter if not remove
# - iterate through a string and count length of that word,
# - check if teh dictionary already contains a word taht is that long
#  - if the dictionar's key exist
# - if yes increment the value by on
# - if not add to the dictionary


def word_sizes(str):
    counted_words = {}
    punctuation = ["!", ".", ",", "?", ":", ";"]
    words = str.split()

    for word in words:
        if word[-1] in punctuation:
            word = word[0:-1]

        counted_words[len(word)] = (
            counted_words[len(word)] + 1 if len(word) in counted_words else 1
        )

    return counted_words


print(word_sizes("Four score and seven."))

# word_sizes('Four score and seven.') #== { 3 => 1, 4 => 1, 5 => 1, 6 => 1 }
# word_sizes('Hey diddle diddle, the cat and the fiddle!') #== { 3 => 5, 6 => 1, 7 => 2 }
# word_sizes("What's up doc?") #== { 6 => 1, 2 => 1, 4 => 1 }
# word_sizes('') == #{}

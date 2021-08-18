# Group Anagrams
# Given the array...

# Copy Code


words = [
    "demo",
    "none",
    "tied",
    "evil",
    "dome",
    "mode",
    "live",
    "fowl",
    "veil",
    "wolf",
    "diet",
    "vile",
    "edit",
    "tide",
    "flow",
    "neon",
]
# Write a program that prints out groups of words that are anagrams. Anagrams are words that have the same exact letters in them but in a different order. Your output should look something like this:

# Copy Code
# ["demo", "dome", "mode"]
# ["neon", "none"]
# #(etc)

# 1. group anagrams together
# - i []
# - [[],[]]
# - take the first word and place it in a new nested array (check if it exist already)
# - iterate through remaining word
# - check if a word A is an anagram of word B
# - if yes push it to an array
# - if not continue to the next word
# - continue until the end of the array
# - take another word
# - check if it exist in any of the nested arrays
# 2. iterate through array of arrays
#    - check if the el exist in the current array
#    - if yes return true false otherwise

# - if it exist just continue and do nothing
# - if it doesn't exist
# - place it in a new, nested array
# - start iterateion from abc import abstractproperty
# from the next word and check if word A and word B are anagrams
# - if they are push it to the abstractproperty
# - if not continue


# 2. print the groups in separate lines
# - iterate through array of arrays
# - print each array


def is_in_list(word, nested_list):
    if not len(nested_list):
        return False

    for li in nested_list:
        if word in li:
            return True
    return False


def is_anagram(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))


def print_groups(nested_list):
    for arr in nested_list:
        print(arr)


def anagram_groups(arr_words):
    final_arr = []

    index = 0
    for word in arr_words:
        if not is_in_list(word, final_arr):
            final_arr.append([word])
            for word_b in arr_words:
                if word_b != word and is_anagram(word, word_b):
                    final_arr[index].append(word_b)
            index += 1
    print_groups(final_arr)


anagram_groups(words)

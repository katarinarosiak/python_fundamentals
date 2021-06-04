# // /Combine Two Lists
# // Write a function that combines two arrays passed as arguments, and returns a new array that contains all elements from both array arguments, with each element taken in alternation.

# // You may assume that both input arrays are non-empty, and that they have the same number of elements.

# // Example:

# // Copy Code


def interleave(arr1, arr2):
    newArr = []

    if len(arr1) > len(arr2):
        longer = arr1
    else:
        longer = arr2
    i = 0
    for elem in longer:

        newArr.append(arr1[i])
        newArr.append(arr2[i])
        i += 1
    return newArr


print(interleave([1, 2, 3], ["a", "b", "c"]))

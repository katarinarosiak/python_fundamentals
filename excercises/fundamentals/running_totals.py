# Running Totals
# Write a method that takes an Array of numbers, and returns an Array with the same number of elements, and each element has the running total from the original Array.

# Examples:
# i: arr
# o: a

# algo:
# - iterate through input arr
# -  take a current element, sum the element with other e from the array, and append it to the array.
# - continue until the end of the array
# test cases:
# - [] => []
# - [1] => [1]


def running_total(arr):
    all_total_run = []
    for i in arr:
        if len(all_total_run) > 0:
            all_total_run.append(all_total_run[-1] + i)
        else:
            all_total_run.append(i)
    return all_total_run


print(running_total([2, 5, 13]) == [2, 7, 20])
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])
print(running_total([3]) == [3])
print(running_total([]) == [])

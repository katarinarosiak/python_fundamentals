# Multiples of 3 and 5
# Write a method that searches for all multiples of 3 or 5 that lie between 1 and some other number, and then computes the sum of those multiples. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

# Examples

# Rules:
# - argumnet is an integer grater than 1
# - find all multiples of 3 or 5 between 1 and the input number
# - add those multiples
# - multiples of either 3 or 5
# - including 20


# Algo:
# produce a set with all multiples of either 3 or 5
#   for all numbers in a range of 1 to 20
#   check if the number is equaly divisible by 3 or by 5
# sum all the numbers
# return


def multisum(num):
    multiples = [i for i in range(1, num + 1) if i % 3 == 0 or i % 5 == 0]
    return sum(multiples)


print(multisum(3))
print(multisum(5))
print(multisum(10))
print(multisum(1000))

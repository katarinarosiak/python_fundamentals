# Fibonacci Number Location By Length
# The Fibonacci series is a series of numbers (1, 1, 2, 3, 5, 8, 13, 21, ...) such that the first 2 numbers are 1 by definition, and each subsequent number is the sum of the two previous numbers. This series appears throughout the natural world.

# Computationally, the Fibonacci series is a very simple series, but the results grow at an incredibly rapid rate. For example, the 100th Fibonacci number is 354,224,848,179,261,915,075 -- that's enormous, especially considering that it takes 6 iterations before it generates the first 2 digit number.

# Write a method that calculates and returns the index of the first Fibonacci number that has the number of digits specified as an argument. (The first Fibonacci number has index 1.)

# Examples:

# Copy Code
# find_fibonacci_index_by_length(2) == 7          # 1 1 2 3 5 8 13
# find_fibonacci_index_by_length(3) == 12         # 1 1 2 3 5 8 13 21 34 55 89 144
# find_fibonacci_index_by_length(10) == 45
# find_fibonacci_index_by_length(100) == 476
# find_fibonacci_index_by_length(1000) == 4782
# find_fibonacci_index_by_length(10000) == 47847
# You may assume that the argument is always greater than or equal to 2.


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1.
# //2.
# //3.
# //Input:
# //- number (num of digits )
# //Output:
# //- number (index of that fibonacci num that has that num of digits )
# //RULES:
# // Explicit:
# //- first 2 num 1,1
# //- eahc subsequent num is sum of two previous numbers
# //- the arg is always greater or equal to 2
# //-
# //-Implicit
# //-
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
# //=> [1 1 2 3 5 8]
# // --------------- DIFFERENT SOLUTIONS --------------------------------
# //MENTAL MODEL:
# //*
# //DATA STRUCTURES:
# // ------------------------  ALGORYTHM:  -----------------------------
# //-  declarate and arr [0, 1 1 2 3 5 8]
#      generate next fibonacci num
#      - take the last el of arr
# //-  check num of digits
# //-  if is equal to arg return indx of that number
# //-  else continue and generate next fib nu
# //-
# //- generate fuboncacci
# //- take two last numbers from and arr
# //-  sum
# //-  push to arr
# //  ---------------------  PSEUDOCODE:  ------------------------------
# //
# //
# //
# //
# //
# //
# //
# // -------------------------------- CODE:  -----------------------------


def find_fibonacci_index_by_length(digits):
    fibonacci = [0, 1, 1, 2, 3, 5, 8]

    while True:
        generate_next_fibonacci(fibonacci)
        lastFibo = len(str(fibonacci[-1]))
        if lastFibo == digits:
            return len(fibonacci) - 1


def generate_next_fibonacci(fibonacci):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


print(find_fibonacci_index_by_length(2))  # == 7          # 1 1 2 3 5 8 13
print(
    find_fibonacci_index_by_length(3)
)  # == 12         # 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(10))  # == 45
print(find_fibonacci_index_by_length(100))  # == 476
print(find_fibonacci_index_by_length(1000))  # == 4782
print(find_fibonacci_index_by_length(10000))  # == 47847

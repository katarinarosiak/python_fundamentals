# 1000 Lights
# You have a bank of switches before you, numbered from 1 to n. Each switch is connected to exactly one light that is initially off. You walk down the row of switches and toggle every one of them. You go back to the beginning, and on this second pass, you toggle switches 2, 4, 6, and so on. On the third pass, you go back again to the beginning and toggle switches 3, 6, 9, and so on. You repeat this process and keep going until you have been through n repetitions.

# Write a method that takes one argument, the total number of switches, and returns an Array that identifies which lights are on after n repetitions.

# Example with n = 5 lights:

# round 1: every light is turned on
# round 2: lights 2 and 4 are now off; 1, 3, 5 are on
# round 3: lights 2, 3, and 4 are now off; 1 and 5 are on
# round 4: lights 2 and 3 are now off; 1, 4, and 5 are on
# round 5: lights 2, 3, and 5 are now off; 1 and 4 are on
# The result is that 2 lights are left on, lights 1 and 4. The return value is [1, 4].

# With 10 lights, 3 lights are left on: lights 1, 4, and 9. The return value is [1, 4, 9].
# 1
# 2
# 3
# 4

# [1,2x,3x,4,5x]
# [true, true, true, true]
# [0-4]
# [1,4]   range(1,5,2)
# [2]
# [3]
# [4]


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1.
# //2.
# //3.
# //Input:
# //- number - total number of switches
# //Output:
# //-  array with switches numbers that are on
# //RULES:
# // Explicit:
# //-
# //-
# //-
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
# //=>
# // --------------- DIFFERENT SOLUTIONS --------------------------------
# //MENTAL MODEL:
# //*
# //DATA STRUCTURES:
# // ------------------------  ALGORYTHM:  -----------------------------
# //- create an array of n length filled with False
# //- iterate through n times
#      - itereate through the arr with step 1
#      - check if the element is true
#      - if yes, change to false
#      - otherwise change to true
# //- for each iteration increment step by 1
# //- return an array with indexes of all elements that are true and add 1.
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


def switcher(switch_num):
    switches = [False] * switch_num
    start = 0
    step = 1
    for i in range(switch_num):
        for idx in range(start, switch_num, step):
            if switches[idx]:
                switches[idx] = False
            else:
                switches[idx] = True
        step += 1
        start += 1
    return [idx + 1 for idx, switch in enumerate(switches) if switch]


# [1,2x,3x,4x,5]
# [true, true, true, true]
# [0-4]
# [1,3]   range(1,5,2)
# [2]     range(2,5,3)
# [3]       (3,5,4)
# [4]       (4,5,5)

print(switcher(5))  # [True, False, false, True, False]

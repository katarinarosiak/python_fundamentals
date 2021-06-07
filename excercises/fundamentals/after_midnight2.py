# After Midnight (Part 2)
# As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write two methods that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both methods should return a value in the range 0..1439.

# You may not use ruby's Date and Time methods.


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
# //- number
# //RULES:
# // Explicit:
# //- need two methodods: that takes time of the day in hours format returns num of minutes 0..1439
# - aftermidnight, before_midnight
# //- the value in range
# //-Implicit
# //- not negative!
# //- don't use methods
# How to count minutes to hours ?
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
# //=>  0:12 => after_midnight => 12     /before_midnight => 23  : 48
# //=>  10 => 0:10, 70, => 70/60 => 1 , 70-60*1 => 10
# //=>  150 => 2 150 - (60*2) => 2:30  => 2*60 => 120 + 30 = 150
# // => 12:34 => 12* 60 + 34 => 754
#   => 12:34  754 =>    /1440 - 754 => 686
# //output:
# //=>
# //=>
# //=>
# // --------------- DIFFERENT SOLUTIONS --------------------------------
# //MENTAL MODEL:
# //*
# //DATA STRUCTURES:
# // ------------------------  ALGORYTHM:  -----------------------------
# //-  before_midnight
# //- take the string and extract number of hours and minutes and coerce to a number
# //- hours multiple by 60 and add minutes
# # //- then substract it from 1440 (num of minutes in 24h)
# //- after_midnight
# //- take the string and extract number of hours and minutes and coerce to a number
# //- hours multiple by 60 and add minutes then return
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


def after_midnight(time):
    if time == "24:00":
        return 0

    time = time.split(":")
    total_min = (int(time[0]) * 60) + int(time[1])

    return total_min


def before_midnight(time):
    if time == "00:00":
        return 0

    time = time.split(":")
    total_min = (int(time[0]) * 60) + int(time[1]) - 1440
    return total_min * -1


# Examples:


print(after_midnight("00:00") == 0)
print(before_midnight("00:00") == 0)
print(after_midnight("12:34") == 754)
print(before_midnight("12:34") == 686)
print(after_midnight("24:00") == 0)
print(before_midnight("24:00") == 0)

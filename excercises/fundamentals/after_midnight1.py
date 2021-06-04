# After Midnight (Part 1)
# The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

# Write a method that takes a time using this minute-based format and returns the time of day in 24 hour format (hh:mm). Your method should work with any integer input.

# You may not use ruby's Date and Time classes.


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1.if the number of min is + the time is after midnight
# //2.if the num of minutes is - the time is before midnight
# //3.
# //Input:
# //- time  (minute based format), any integer (-,+,0)
# //Output:
# //- time of the day 24h format (hh:mm) string
# //RULES:
# // Explicit:
# //- integers , +, -, and 0
# //- .if the number of min is + the time is after midnight
# //- if the num of minutes is - the time is before midnight
# //-
# //-Implicit
# //- need to count how how many hours and minutes is the input
# //-
# // EDGE CASES:
# // => time_of_day(0) == "00:00"
# time_of_day(-3) == "23:57" // 24:60  if imput is less than 60 => 60-input
# -145 => -145/60 -2,433.. => -2 / 433.. roundit 0,433
# time_of_day(35) == "00:35" // 00:00 => 00:60, 00:00 => 00:35
# // =>   time_of_day(-1437) == "00:03" // how many minutes and hours are in the input?
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
# //DATA STRUCTURES: number, string, object
# // ------------------------  ALGORYTHM:  -----------------------------
# //-
# //- if 0 return 00:00
# count number if minutes to hours:
# //- take the input and divide it by 60 then remove reminder = this will give us hours
# //- take the reminder and round it and then multiply by 60 and the round this will gve us minutes
# Deduct or add:
# //- if hours are negative:
#        - deduct them from 24
#           - is the result grater than 48?
#           - if no:
#                 -if it gives negative number remove sign
#           if yes:
#                 -
#        - and deduct minutes from 60
# //- if positive
# //-    - add them to 00
# //-    - add minutes to 00
# //-     - what if hours or minutes more than 12 or 60 ?
# //  ---------------------  PSEUDOCODE:  ------------------------------
# //
# //
# //
# //
# //
# //
# //
# // -------------------------------- CODE:  -----------------------------


def formatHours(hours, minutes):
    hours = str(hours)
    minutes = str(minutes)

    if len(hours) == 1:
        hours = "0" + hours

    if len(minutes) == 1:
        minutes = "0" + minutes

    return f"{hours}:{minutes}"


def time_of_day(num):
    day_in_min = 1440

    reminder = (num / 1440) % 1
    hours = int((reminder * day_in_min) / 60)
    minutes = int(round(((reminder * day_in_min / 60) % 1) * 60, 0))

    return formatHours(hours, minutes)


# Examples:

print(time_of_day(0))  # == "00:00"
print(time_of_day(-3))  # == "23:57"
print(time_of_day(35))  # == "00:35"
print(time_of_day(-1437))  # == "00:03"
print(time_of_day(3000))  # == "02:00"
print(time_of_day(800))  # == "13:20"
print(time_of_day(-4231))  # == "01:29"

# Cute angles
# Write a method that takes a floating point number that represents an angle between 0 and 360 degrees and returns a String that represents that angle in degrees, minutes and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. A degree has 60 minutes, while a minute has 60 seconds.

# Examples:

# Copy Code
# dms(30) == %(30°00'00")
# dms(76.73) == %(76°43'48")
# dms(254.6) == %(254°36'00")
# dms(93.034773) == %(93°02'05")
# dms(0) == %(0°00'00")
# dms(360) == %(360°00'00") || dms(360) == %(0°00'00")
# Note: your results may differ slightly depending on how you round values, but should be within a second or two of the results shown.

# You should use two digit numbers with leading zeros when formatting the minutes and seconds, e.g., 321°03'07".

# You may use this constant to represent the degree symbol:

# Copy Code
# DEGREE = "\xC2\xB0"


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1.
# //2.
# //3.
# //Input:
# //- float
# //Output:
# //- string
# //RULES:
# // Explicit:
# //- floating point num represents an angle between 0 - 360
# //- use two digit numbers with leading zeros when formatting the minutes and seconds,
# //- DEGREE = "\xC2\xB0"
# //-
# //-Implicit
# //- degrees stays the same , we need to calculate the floating point
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
# //=> (76.73) == %(76°43'48")
# //=> 76  73
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
# //- extract the integer
# //- extract float
# //- 60X float = minutes
# //- take the float and 60X float = seconds
# //-
# //-
# //-
# //-
# //-
# //  ---------------------  PSEUDOCODE:  ------------------------------
# //
# // °
# //
# //
# //
# //
# //
# // -------------------------------- CODE:  -----------------------------

import math


def stringify(num):
    if num == 60 or num == 0:
        return "00"
    elif num < 10:
        return f"0{num}"
    else:
        return num


def dms(angle):
    degree = int(angle)
    minutes = angle % 1 * 60
    seconds = round(minutes % 1 * 60)
    minutes = round(minutes)
    sec = '"'

    return f"{degree}°{stringify(minutes)}'{stringify(seconds)}{sec}"


# Copy Code
# print(dms(30))  # == %(30°00'00")
print(dms(76.73))  # == %(76°43'48")
# print(dms(254.6))  # == %(254°36'00")
# print(dms(93.034773))  # == %(93°02'05")
# print(dms(0))  # == %(0°00'00")
# print(dms(360))  # == %(360°00'00") || dms(360) == %(0°00'00")
# Note: your results may differ slightly depending on how you round values, but should be within a second or two of the results shown.

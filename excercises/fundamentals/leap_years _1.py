# Leap Years (Part 1)
# In the modern era under the Gregorian Calendar, leap years occur in every year that is evenly divisible by 4, unless the year is also divisible by 100. If the year is evenly divisible by 100, then it is not a leap year unless the year is evenly divisible by 400.

# Assume this rule is good for any year greater than year 0. Write a method that takes any year greater than 0 as input, and returns true if the year is a leap year, or false if it is not a leap year.


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1.
# //2.
# //3.
# //Input:
# //- number
# //Output:
# //-  boolean
# //RULES:
# // Explicit:
# //- if the year is evenly divisble by 100 and 400 = leap year
# //- if the year is evenly divisible by 100 but not 400 = it is not leap year
# //- every year that is evenly divisible by 4 but not by 100 = leap year
# //- the input will be a integer greater than 0
#    if 100 and 400 true
#    if 4 and !100
# //-Implicit
# //-
# //-
# // EDGE CASES:
# // => 400 => true , 800 true, 1600 true , 2000 true,
# // => 100 => false, 200 false, 600 false, 2100 false,
# // => 4 true, 8 true, 12 true 200 = false,
#    => 1, 2, 3 => false
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
# // => 400 => true , 800 true, 1600 true , 2000 true,
# // => 100 => false, 200 false, 600 false, 2100 false,
# // => 4 true, 8 true, 12 true 200 = false,
#    => 1, 2, 3 => false
# print(leap_year(1) == False)
# print(leap_year(2) == False)
# print(leap_year(4) == True)
# print(leap_year(8) == True)
# print(leap_year(12) == True)
# print(leap_year(200) == False)
# print(leap_year(100) == False)
# print(leap_year(600) == False)
# print(leap_year(2100) == False)
# print(leap_year(400) == True)
# print(leap_year(800) == True)
# print(leap_year(1600) == True)
# print(leap_year(2000) == True)
# print(leap_year(400) == True)

# // --------------- DIFFERENT SOLUTIONS --------------------------------
# //MENTAL MODEL:
# //*
# //DATA STRUCTURES:
# // ------------------------  ALGORYTHM:  -----------------------------
# //- check if the number is divisible by 100 and 400 and if yes return true
# //- else check if it is divisible by 4 and not 100, if yes return true,
# //- else return false
# //-
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


def leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and not year % 100 == 0:
        return True
    else:
        return False


# print(leap_year(1) == False)
# print(leap_year(2) == False)
# print(leap_year(4) == True)
# print(leap_year(8) == True)
# print(leap_year(12) == True)
# print(leap_year(200) == False)
# print(leap_year(100) == False)
# print(leap_year(600) == False)
# print(leap_year(2100) == False)
# print(leap_year(400) == True)
# print(leap_year(800) == True)
# print(leap_year(1600) == True)
# print(leap_year(2000) == True)
# print(leap_year(400) == True)

# print(leap_year(2016) == True)
# print(leap_year(2015) == False)
# print(leap_year(2100) == False)
# print(leap_year(2400) == True)
# print(leap_year(240000) == True)
# print(leap_year(240001) == False)
# print(leap_year(2000) == True)
# print(leap_year(1900) == False)
# print(leap_year(1752) == True)
# print(leap_year(1700) == False)
# print(leap_year(1) == False)
# print(leap_year(100) == False)
# print(leap_year(400) == True)

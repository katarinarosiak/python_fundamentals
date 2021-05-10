# What Century is That?
# Write a method that takes a year as input and returns the century. The return value should be a string that begins with the century number, and ends with st, nd, rd, or th as appropriate for that number.

# New centuries begin in years that end with 01. So, the years 1901-2000 comprise the 20th century.


# //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PEDAC ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //
# // ------------------  UNDERSTAND THE PROBLEM:  -------------------
# //1. create a function taht takes an integer (a year) as a argument and calcualte which century that would be, then it returns a sring with the century and adequate ending
# //2.
# //3.
# //Input:
# //- integer
# //Output:
# //- str
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
#   => 1 => 1st
#   => 100 => 1st
#   => 101 => 2nd
#   => 200 => 2nd
#   => 201 => 3rd
#   => 10 => 1st
#   => 99 => 1st
#   => 765 => 8th
#   => 700 => 7th
# //=> 1956 => 20th,
# //=> 1900 => 19th
#   => 1901 => 20th
#   => 2099 => 21th
#   => 2100 => 21th
#   => 2101 => 22nd
#   => 3456 => 35th
#   => 3400 => 34th
#   => 14900 => 150th
#   => 16001 => 161st
#   => 116001 => 1161st
#   => 2890765 => 28907.65 => 28908th
#   => 0 => 0
# //=> 201 => 3rd
#  => 200 => 2nd
#  =>
# //output:
# //=>
# //=>
# //=>
# // --------------- DIFFERENT SOLUTIONS --------------------------------
# //MENTAL MODEL:
# //*
# //DATA STRUCTURES:
# // ------------------------  ALGORYTHM:  -----------------------------
# //- detemin which century will the year be
#       - divide year by 100
#       - if no reminder add 1
# //- depending on the century add adequate ending
# //- create a dictionary with number and corresponding ending
# //- determin the last two digits
# //- add the ending
# //- >= 04 = 20 th, , else  00 = th, 01 = st, 02 => nd, 03 => rd, >= 04 = 20 th,
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


def century(year):

    if year % 100 == 0:
        century = int(year / 100)
    else:
        century = int(year / 100 + 1)
    return abr(century)


def abr(century):
    endings = {
        "1": "st",
        "2": "nd",
        "3": "rd",
    }

    last_two_num = century % 100
    last_num = str(last_two_num)[-1]
    cent_str = str(century)

    if last_two_num >= 4 and last_two_num <= 20:
        return cent_str + "th"
    else:
        if last_num in endings:
            return cent_str + endings[last_num]
        else:
            return cent_str + "th"


print(century(2000) == "20th")
print(century(2001) == "21st")
print(century(1965) == "20th")
print(century(256) == "3rd")
print(century(1) == "1st")
print(century(10103) == "102nd")
print(century(1052) == "11th")
print(century(1127) == "12th")
print(century(11201) == "113th")

# Leap Years (Part 2)
# A continuation of the previous exercise.

# The British Empire adopted the Gregorian Calendar in 1752, which was a leap year. Prior to 1752, the Julian Calendar was used. Under the Julian Calendar, leap years occur in any year that is evenly divisible by 4.

# Using this information, update the method from the previous exercise to determine leap years both before and after 1752.


def leap_year(year):
    if year >= 1752:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 4 == 0 and not year % 100 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(leap_year(2016) == True)
print(leap_year(2015) == False)
print(leap_year(2100) == False)
print(leap_year(2400) == True)
print(leap_year(240000) == True)
print(leap_year(240001) == False)
print(leap_year(2000) == True)
print(leap_year(1900) == False)
print(leap_year(1752) == True)
print(leap_year(1700) == True)
print(leap_year(1) == False)
print(leap_year(100) == True)
print(leap_year(400) == True)

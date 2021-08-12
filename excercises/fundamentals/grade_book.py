# Grade book
# Write a method that determines the mean (average) of the three scores passed to it, and returns the letter value associated with that grade.

# Numerical Score Letter	Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

# Example:

# Copy Code
# get_grade(95, 90, 93) == "A"
# get_grade(50, 50, 95) == "D"


def avg(tup):
    return sum(tup) / len(tup)


def get_grade(*tup):
    grades = {
        "A": range(90, 100),
        "B": range(80, 89),
        "C": range(70, 79),
        "D": range(60, 69),
        "F": range(0, 59),
    }
    for lit in grades:
        if int(avg(tup)) in grades[lit]:
            return lit


print(get_grade(95, 90, 93) == "A")
print(get_grade(50, 50, 95) == "D")

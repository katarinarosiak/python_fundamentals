# Write a program that solicits 6 numbers from the user, then prints a message that describes whether or not the 6th number appears amongst the first 5 numbers.


numbers = []


def ending(i):
    switcher = {
        1: "st",
        2: "nd",
        3: "rd",
    }
    return switcher.get(i, "th")


for i in range(7):
    numbers.append(input(f"Enter the {i}{ending(i)} number: "))

if numbers[-1] in numbers[0:-1]:
    print(f"{numbers[-1]} exist among other numbers.")
else:
    print(f"{numbers[-1]} doesn't exist among other numbers")

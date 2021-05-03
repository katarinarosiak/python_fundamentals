# When will I Retire?
# Build a program that displays when the user will retire and how many years she has to work till retirement.

# Example:

# Copy Code
# What is your age? 30
# At what age would you like to retire? 70

# It's 2016. You will retire in 2056.
# You have only 40 years of work to go!
import datetime
age = int(input('How old are you?'))
retirement = 65
date = datetime.datetime.now()
when = (retirement - age) + date.year
print(f"You will retire in {when}")

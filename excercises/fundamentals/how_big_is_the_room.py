# How big is the room?
# Build a program that asks a user for the length and width of a room in meters and then displays the area of the room in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# Do not worry about validating the input at this time.

# Example Run

# Enter the length of the room in meters:
# 10
# Enter the width of the room in meters:
# 7
# The area of the room is 70.0 square meters (753.47 square feet).

room_length = input('Enter the length of the room in meters: ')
room_width = input('Enter the width of the room in meters: ')

FEET_CONST = 10.764
square_space = float(room_length) * float(room_width)

square_feet = square_space * FEET_CONST
#square_feet = float("{0:.2f}".format(square_feet))

print(f"The are of the room is {square_space} square meters ({square_feet} square feet)")
# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip and then display both the tip and the total amount of the bill.

# Example:

# Copy Code
# What is the bill? 200
# What is the tip percentage? 15

# The tip is $30.0
# The total is $230.0

bill = int(input('What is the bill? '))
tip = int(input('What is the tip percentage? '))
tip_total = bill * (tip*0.01)

print(f"The tip is {tip_total}")
print(f"The total is ${(tip_total) + bill}")

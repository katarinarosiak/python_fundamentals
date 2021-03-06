# Grocery List
# Write a method which takes a grocery list (array) of fruits with quantities and converts it into an array of the correct number of each fruit.

# Example:

# Copy Code
# buy_fruit([["apples", 3], ["orange", 1], ["bananas", 2]]) ==
#   ["apples", "apples", "apples", "orange", "bananas","bananas"]


def buy_fruit(fruits):
    return (
        " ".join([(innerArr[0] + " ") * innerArr[1] for innerArr in fruits])
    ).split()


print(buy_fruit([["apples", 3], ["orange", 1], ["bananas", 2]]))

# ASCII String Value
# Write a method that determines and returns the ASCII string value of a string that is passed in as an argument. The ASCII string value is the sum of the ASCII values of every character in the string.


def ascii_value(text):
    ascii = [ord(i) for i in text]
    return sum(ascii)


print(ascii_value("Four score") == 984)
print(ascii_value("Launch School") == 1251)
print(ascii_value("a") == 97)
print(ascii_value("") == 0)

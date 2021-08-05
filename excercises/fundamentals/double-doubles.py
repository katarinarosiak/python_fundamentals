# Double Doubles
# A double number is a number with an even number of digits whose left-side digits are exactly the same as its right-side digits. For example, 44, 3333, 103103, 7676 are all double numbers. 444, 334433, and 107 are not.

# Write a method that returns 2 times the number provided as an argument, unless the argument is a double number; double numbers should be returned as-is.

# Examples:

# Copy Code
# twice(37) == 74
# twice(44) == 44
# twice(334433) == 668866
# twice(444) == 888
# twice(107) == 214
# twice(103103) == 103103
# twice(3333) == 3333
# twice(7676) == 7676
# twice(123_456_789_123_456_789) == 123_456_789_123_456_789
# twice(5) == 10
# Note: underscores are used for clarity above. Ruby lets you use underscores when writing long numbers; however, it does not print the underscores when printing long numbers. Don't be alarmed if you don't see the underscores when running your tests.


def twice(num):

    if is_doubble_num(num):
        return num
    else:
        return num * 2


def is_doubble_num(num):
    num_str = str(num)

    if len(num_str) % 2 == 0:
        half = int(len(num_str) / 2)
        return num_str[(half * -1) :] == num_str[0:half]
    else:
        return False


print(twice(37) == 74)
print(twice(44) == 44)
print(twice(334433) == 668866)
print(twice(444) == 888)
print(twice(107) == 214)
print(twice(103103) == 103103)
print(twice(3333) == 3333)
print(twice(7676) == 7676)
print(twice(123_456_789_123_456_789) == 123_456_789_123_456_789)
print(twice(5) == 10)

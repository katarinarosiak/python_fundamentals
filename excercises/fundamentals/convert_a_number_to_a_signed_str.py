def integer_to_string(num):
    lib = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numerals = []
    divider = 10
    integers = []
    final_str = ""

    while True:
        current = num % divider
        numerals.append(current)
        divider = divider * 10

        if current == num:
            break

    divider = 1
    for i in numerals:
        integers.append(int(i / divider))
        divider *= 10

    integers.reverse()

    for i in integers:
        final_str += lib[i]
    return final_str


def signed_integer_to_string(num):

    if num < 0:
        return f"-{integer_to_string(num*-1)}"
    elif num > 0:
        return f"+{integer_to_string(num)}"
    else:
        return "0"


print(signed_integer_to_string(4321) == "+4321")
print(signed_integer_to_string(-123) == "-123")
print(signed_integer_to_string(0) == "0")

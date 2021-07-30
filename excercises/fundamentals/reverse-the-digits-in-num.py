# Reverse the Digits In a Number
# Write a method that takes a positive integer as an argument and returns that number with its digits reversed. Examples:

# Copy Code
# reversed_number(12345) == 54321
# reversed_number(12213) == 31221
# reversed_number(456) == 654
# reversed_number(12000) == 21 # No leading zeros in return value!
# reversed_number(12003) == 30021
# reversed_number(1) == 1
# Don't worry about arguments with leading zeros - Ruby sees those as octal numbers, which will cause confusing results. For similar reasons, the return value for our fourth example doesn't have any leading zeros.


def reversed_number(num):
    return int("".join(list(reversed(str(num)))))


print(reversed_number(12345) == 54321)
print(reversed_number(12213) == 31221)
print(reversed_number(456) == 654)
print(reversed_number(12000) == 21)  # No leading zeros in return value!
print(reversed_number(12003) == 30021)
print(reversed_number(1) == 1)

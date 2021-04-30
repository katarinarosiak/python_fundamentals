
# Write a function that takes one integer argument, which may be positive, negative, or zero. This method returns true if the number's absolute value is odd. You may assume that the argument is a valid integer value.

def is_odd(num):
  return abs(num) % 2 != 0


print(is_odd(2)); # => False
print(is_odd(5)); # => True
print(is_odd(-17)); # => True
print(is_odd(-8)); # => False
print(is_odd(0)); # => False
print(is_odd(7)); # => True
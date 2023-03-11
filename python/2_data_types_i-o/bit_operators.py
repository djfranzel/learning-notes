
# these are actually the same in the binary system, but the only ones!
first_bit = 1
second_bit = 1

print(first_bit & second_bit)
print(first_bit | second_bit)
print(first_bit ^ second_bit)
print(~0)

# bit shift
# this shifts the bit representation to the left/right and outputs the results
print(12 << 1)
print(12 << 2)

# way to remember this is the shift is by the right number to the power of 2
# left and right shift correlate to * or / by the number of shifts to the power of 2
print((12 << 2) == 12 * (2 ** 2))
print((12 >> 2) == 12 / (2 ** 2))

# when the number isn't an int, it doesn't work as in the second example
print((12 << 3) == 12 * (2 ** 3))
print((12 >> 3) == 12 / (2 ** 3))
print(12 >> 3)
print(12 / (2 ** 3))

# bits are stored in binary, which represents a number starting from the right side
# the number 12 in binary is 1100
# starting from the right, 1 then 2 then 4 then 8, doubling each step to the left
# when 0, don't count the number, when 1, count it
# 1 is 0, nope, 2 is 0, nope, 3 is 1, yep, 4 is 1, yep
# so the place of 3 and 4, which are 4 and 8, equals 12


# I definitely need more practice on bit operators, as I am not familiar with them at all


# assertions!!

# use assertions for debugging and testing, not for validating user input
# should NOT be handled with try/except blocks
# use for documentation, debugging, testing only
def calculate_inverse(number):
    assert (number != 0), 'Got 0!'
    return 1/number

# print(calculate_inverse(0))


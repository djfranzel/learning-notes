
import math

def halve_string(input_string):
    # cut string in half, with first larger if char count is odd
    first_half = input_string[:math.ceil(len(input_string)/2)]
    last_half = input_string[math.ceil(len(input_string)/2):]
    return (first_half, last_half)

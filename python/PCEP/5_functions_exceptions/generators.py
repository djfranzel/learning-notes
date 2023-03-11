
# generators! I have no idea what these are

def get_number():
    for i in range(1, 4):
        yield i

# functions become generators when you use 'yield' instead of 'return'

# must call the 'next' function to get the yield of the function
# when the function runs, it remembers the previous values in the function
# then next calls the next iteration, depending on if it is valid

generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))
# or
for x in get_number():
    print(x)

# or
numbers = list(get_number())
print(numbers)

# it wasn't till the last example that I could see any uses here
# could generate complex lists with this, which might be useful

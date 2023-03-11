
# functions! 
def greet():
    print('Hello!')

greet() # this is as basic as possible

# function with parameters
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print(average)

get_average([5.0, 3.5, 7.8, 9.9, 10.0])

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count('Welcome', 'e')
print_letter_count(letter='e', text='Welcome') # I like this! what are the limits to declaring vars?

# these are optional arguments at the end for the print function
# can use them or not, and they always have default values!
print('Hello', 'How are you?', end='.', sep='-')

# this function now is defined to have a default value, yet still set-able to 'a'
# caveat! must provide default ones at the END, won't work if you set at beginning
# likely no technical reason, probably aesthetic
def print_letter_count(text, letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

print_letter_count('David Franzel')
# all positional arguments must be first, before optional arguments

# shadowing! 
# the variable set within the function does not set the variable outside the function
# this is different from javascript, although perhaps not if you consider the variable
# is re-instantiated within the function, not setting the other one
# in javascript, you can prefix with 'var'/'let'/'const' to tell the computer if you are 
# redeclaring, in python you have no option, just redeclaring it, more simple, but tradeoffs for sure
def show_truth():
    # global means don't shadow! the shadow is when this is redeclared in a different scope and so doesn't modify in the other scope
    global mysterious_var # this references the var one layer up and then modifies it in the next line
    mysterious_var = 'New Surprise!'
    print(mysterious_var)

mysterious_var = 'Surprise!'
print(mysterious_var)
show_truth()
print(mysterious_var)

# some functions return a value, some do something as their use

print_return = print('Hi!')
print(print_return) # this returns 'None', which is probably just like 'void' in java

# to get a function to return 'None', either don't specify a return, or just have 'return' with nothing following

x = None 
if x is None: 
    print('yes!')
if x == None:
    print('yay 2!')


def greet():
    print('hello!')

x = greet()
print(x)

# coding exercise for getting unique numbers
# was tricky and had to get a hint! not that hard, so oh well
def unique(numbers=[]):
    unique_list = []
    for number in numbers:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list

print(unique([1,1,4,5,1]))
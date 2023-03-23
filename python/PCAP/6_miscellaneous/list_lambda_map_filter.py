
# list comprehensions
one_to_hundred = [val for val in range(1, 101) if val % 5 == 0]
print(one_to_hundred)

numbers = [0 if i % 2 == 0 else 1 for i in range(100)]
print(numbers)

table = [[i for i in range(1, 6)] for j in range(5)]
print(table)

# list comp are a great way to set lists easily and programatically instead of manually


# lambda functions

def sum(a, b):
    return a + b

# lambdas can be elegantly assigned to variables
another_sum = lambda a, b: a + b

print(another_sum(1, 3))

def apply_func(elements, func):
    for element in elements:
        print(func(element))

apply_func([i for i in range(5)], lambda a: a + a)

# lambdas allow simple, clear, consise code to be written in certain situations
# not sure where in my code would I put this, but good to know! 


# map() uses
# first takes function, then a sequence of elements
# creates an interator which is accessible by loop or able to convert to list

lambda_func = lambda i: i * 2
initial_list = [i for i in range(1,6)]
map_result = map(lambda_func, initial_list)

for element in map_result:
    print(element, end=',')

# can also convert to list
print(list(map_result))

# in either of these ways above, the original map is deleted - seems like odd behavior

print(list(map(lambda i: i * 2, [1,2,3,4,5])))

# filter is similar, how is it actually different than map?
print(list(filter(lambda i: i % 2 == 0, [i for i in range(100)])))

emails = [
    'frank@gmail.com',
    'i love python',
    '12345676',
    'jonsmith@yahoo.com',
    'whereareyou@mywebsite.co.uk',
    'fdsadfsd'
]

# filter will return the item that matches the provided condition
print(list(filter(lambda x: '@' in x, emails)))

# map will return True/False list showing which items match the condition
print(list(map(lambda x: '@' in x, emails)))


# closures!

def greet(text):

    def print_greet():
        print(text) # by accessing the variable in the parent scope, this function becomes a closure

    return print_greet

say_hello = greet('Hello')
say_hello()
say_hello()

# the 'text' variable normally would be destroyed after the function is done calling
# in closures, these are called 'free variables', they persist while the variable that is the function persists


def make_multiply_closure(x):

    def multiply(y):
        return x * y
    
    return multiply

multiply_5 = make_multiply_closure(5)
multiply_12 = make_multiply_closure(12)

print(multiply_5(10))
print(multiply_12(20))

# closures can be useful in replacing classes with only one method
# generally shorter and easier to read
# some people use a lot of them, others not so much
# good to know the techniques!
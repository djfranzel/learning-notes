
# modules!!

# if calling non-existent function from a module, 'AttributeError' exception occurs

import sys, math
# or
import sys
import math
# can be more specific with imports
from sys import exit
# generally not used, dangerous since function names might be used by your own functions
from sys import * 
# nice shorthand import or alias a specific function
import sys as s
from sys import exit as bye_bye

# this shows all the 'sys' functions that can be called
for name in dir(sys):
    print(name)

import math

for name in dir(math):
    print(name)

# these are some important ones
# ceil(), floot(), trunc()
print(math.ceil(3.6)) # -> 4
print(math.floor(3.6)) # -> 3
print(math.trunc(3.6)) # -> 3
print(math.factorial(3)) # -> 6
print(math.sqrt(16)) # -> 4
print(math.hypot(3,4)) # -> 5


# since code is always a set of logical statements, it cannot easily create randomness
# but, since time is always changing, can use the time as a seed for new randomness
# this creates a psuedo-random result that is effectively random
import random

random.seed(0) # this demonstrates that the seed for generating randomness is always the same when overriding seed source
print(random.random())
print(random.random())
print(random.random())

numbers = [i for i in range(1,11)]
names = ['Alan','Kate','Mary','Kate','Jo','John']

random.seed() # reset the seed from the previous example
print(random.choice(numbers))
print(random.choice(names))
print(random.choice('heythereman')) # outputs random letter
print(random.sample(names, 3))


import platform
print(platform.platform())
print(platform.platform(aliased=False, terse=False)) # these are default values
print(platform.platform(True, True)) # when set to true, we get more condensed output
print(platform.machine())
print(platform.processor())
print(platform.system())
print(platform.python_implementation()) # CPython on my machine, most common way to run python
print(platform.python_version_tuple()) # python version output
print(platform.version()) # prints your platform version, not python!


# coding challenge - this generates some random number sets etc. 
def generate_tickets(ticket_count, max_number):
    
    # this is a cool example of the arguments random.sample can take
    # python is such a module-rich language! I like it
    unique_numbers = random.sample(range(0, max_number), ticket_count)
    
    return (unique_numbers, random.choice(unique_numbers))
    
print(generate_tickets(5, 10))


# we will generate our own modules!
# located in custom_module, and in two files
# when this file is run, a temp python directory called __pycache__ is created
# this has the partially compiled code that is ready to use quickly

# when you import your own module, run it and then python stores the 
# semi-compiled code in __pycache__ , this is mostly compiled and I think
# just needs to be interpreted by the python PVM (not sure on that!)


# python uses a variable to store potential paths for the modules that you import
# called the sys variable!
import sys

# this returns a list of strings which are paths
# each path is checked in order, and as soon as one has the right file, it returns
# first checks parent directory, then some python system files
# print(sys.path)
for path in sys.path:
    print(path)


# if our module isn't in this list, we could add it manually to take advantage of storing ours
sys.path.append('secret') # this is a relative path, points to a directory from this location
# could also add absolute path, but then different systems wouldn't recognize it likely
for path in sys.path:
    print(path)

# PACKAGES!
# this is basically a nice collection of all your modules

# when I import this module below, just the import statement causes __init__.py to run!
# this is useful if you need to initialize module with boilerplate code and 
# don't want that boilerplate to run all the time when calling
# used to be true that __init__.py was required for python to consider a directory a package 3.3 and up not required
# traverse package contents with custom_module.next.next.module for accessing the modules
import custom_module


# namespace - abstract space where names for objects and elements exist

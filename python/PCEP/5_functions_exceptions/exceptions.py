import sys

# exceptions!!

# there are two specific exceptions being caught here
# always try and add the last to catch any general exceptions!
try: 
    value = int(input('Enter integer: '))
    print(1/value)
except ValueError:
    print('not a number!')
except ZeroDivisionError:
    print('cannot divide by zero')
except:
    print('general exception')


user_name = input('name? ')
if user_name == '':
    print('empty')
    sys.exit()
print('Hello,', user_name)

# python will try and raise the most specific exception possible
# these exceptions are needed for the exam
# BaseException
# Exception - broad exception model
# SystemExit - exits the program
# KeyboardInterrupt - user interrupts program with keyboard
# ArithmeticError - broad math errors
# LookupError
# TypeError - wrong data type for an operation
# ValueError - data type might be correct in casting, but 'a' is not a number, where '1' could be casted
# ZeroDivisionError
# IndexError - index does not exist
# KeyError - key does not exist in a dictionary



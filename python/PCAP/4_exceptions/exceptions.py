
# the beginning is a copy of PCEP/exceptions!!
# more advanced exceptions than PCEP
# SyntaxError are caught when you run the program
# you can run 'raise SyntaxError' and then catch it, but try/except blocks will not work to 
# catch the actual error

# the else block will execute if no exception is thrown
# acts like an else for except
# not commonly used, but good to know
try:
    value = int(input('Enter int: '))
    print(1/value)
except:
    print('wrong!')
else:
    print('All good')
finally:
    print('finally!')

# finally will always run, and might work for closing db connections or other tasks

# raise is the same as throw in java and javascript
def return_larger(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError
    if b > a:
        return b
    else:
        return b
    
try:
    return_larger(5, '3')
except ValueError:
    print('value error')
except: 
    print('general exception')
finally:
    print('done!')

print(return_larger(5, 3))

def return_reverse(x):
    try:
        return 1/x
    except:
        print('wrong!')
        raise # raising exception in the except block essentially throws the exception up the chain to be handled up the stack

try:
    return_reverse(0)
except:
    print('error')

def return_bigger(a, b):
    try: 
        if b > a:
            return b
        else:
            return a
    except Exception as e: # this helps to get a more verbose exception output
        print(e)
        return None
    
print(return_bigger(5, 'b'))

# this shows all the subclasses that use Exception as a base for their class
for subclass in Exception.__subclasses__():
    print(subclass.__name__)

# this addition will include a message in the object that can provide specific messages
try:
    raise Exception('exception message')
except Exception as e:
    print(e.args)

# sometimes python will provide more verbose exceptions accessible by .args
try:
    5 < 'a'
except Exception as e:
    print(e.args)


# create custom exception classes!

# by inheriting all the props and variables of ValueError, you can create custom exception
class AnimalValueError(ValueError):
    pass

def produce_animal_sound(animal_type):
    if animal_type == 'DOG':
        print('Woof, woof!')
    elif animal_type == 'Cat':
        print('Meow')
    else:
        raise AnimalValueError('Incorrect animal type')
    
produce_animal_sound('DOG')

# this above one is quite specific, since ValueError is specific
# below is a more general exception class

class UserActionException(Exception):
    def __init__(self, message='', user_id=''):
        super().__init__() # or Exception.__init__(self)
        self.user_id = user_id
        self.message = message

    # we are overriding the __str__ basic method in Exception class to give a custom error message
    # when setting Exception as e, print(e) automatically prints from the __str__ private method
    def __str__(self) -> str:
        return type(self).__name__ + ' occurred. Msg: ' + self.message + ', userId: ' + self.user_id

def say_hello(name, user_id):
    if name == '':
        raise UserActionException('empty name!', user_id)
    print('Hello', name)

try:
    say_hello('Adam', 'DT324')
    say_hello('', 'DTD324')
except Exception as e:
    print(e)


"""" this is a description of this test module for educational purposes """

def test_function(string):
    return string

print('I am a module')

# often this is used to run tests!
# when this file is run with `py own_module`, __main__ is true
# perhaps that is a good time to run tests
# when it is imported, as in ./main.py, it will be 'Executed as module', no tests!
if __name__ == '__main__':
    print('Executed directly')
else:
    print('Executed as module')

# python has no way to make variables private to a module (odd!)
# the convention is to use _ or __ var prefix to tell users never to modify

__test_var = 10

public_var = 'Yay!'
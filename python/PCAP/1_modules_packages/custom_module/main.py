
# when this is imported, python reads the whole file
# any code is executed, more likely the function names are stored in some kind of memory
# if a module imports another module that you import here, 
# python remembers it was already imported and doesn't run it again, nice!
import own_module

# print(own_module.test_function('Hey!'))

# should never! access this __ char, and the autocomplete does not show it as an option
# it does however, work, although is bad practice
print(own_module.__test_var)

print(own_module.public_var)

import lists_utils

my_list = [23, 21, 2, 5, 72]
print(lists_utils.sum_elements(my_list))
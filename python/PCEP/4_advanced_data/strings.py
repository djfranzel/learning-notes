
# more info on strings and manipulation
# IMMUTABLE (int/float are also immutable)
fav_band = 'Green Day'
print(fav_band[6]) # this prints 'D'

print(fav_band[:5]) # this prints from start index to six, stopping at index 4

# fav_band[6] = 'M' # this will fail! python cannot splice strings like this

# these are some common string manipulation methods
# .sort() and sorted() for lists are the reverse syntax for mutating originals or not
text = 'please capitalize me!'
text_cap = text.upper()
print(text_cap)
print(text)

# boolean check to see if number is numeric, or integer only?
# (could have used this instead of try catch in coding assessment!!)
user_number = input('Provide a number: ')
if user_number.isnumeric():
    print('Yay!')
else:
    print('Nay!')

# there are many more string manipulation methods, look them up sometime


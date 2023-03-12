
# strings can be with double quotes, but single quotes is best practice
# one ASCII char takes 8 bits, or 1 byte
# UTF-8 is compatible with ASCII
# uses only as many bits as needed (8-32)
# video goes into theory of how strings are stored, not sure how relevant this is

# basic ops

print(len('hi'))
print('hi there'[1])
print('hi there'[:5])
# etc...

# codepoint of each char can be found (only one char string)
print(ord('a'))
print(chr(97)) # gets you the letter from the codepoint

# multi-line strings
test_string = '''
Hey there!
'''
print(test_string)
print(len(test_string)) # this includes \n as 1 char

print('aaa' + 'bbb')
print(2 * 'bb')

for char in 'hello world':
    print(char, end='-')

# strings are immutable, so no changing strings
# can however reassign them to new full values

print(min('david franzel')) # the min actually looks at the code for each char and returns the lowest
print(max('david franzel'))

print('david franzel'.index('a')) # returns index of first occurence
print('david franzel'.find('c')) # safer to use! returns -1 if not found, while index throws error
print('david franzel'.find('a', 10)) # starts at index 10 inclusive
print('david franzel'.find('a', 5, 10)) # starts at index 5 inclusive, to 10 exclusive
print('david franzel'.rfind('a')) # same potential as .find, but starts at end


print('david123'.isalnum()) # returns bool if string is alphanumberic
# many other helpers like this built in

# join!
# this will join the array with ' ' as the joining char
print(' '.join(['This is','a spectacular','place to be']))

# split!
print('How many\tstrings\nwill you see?'.split())

names_list = ['David', 'Julie', 'Christine']
names_list.sort() # this mutates the original
sorted_names_list = sorted(names_list) # this preserves original and returns the sorted list

# strings can be with double quotes, but single quotes is best practice
# one ASCII char takes 8 bits, or 1 byte
# UTF-8 is compatible with ASCII
# uses only as many bits as needed (8-32)
# video goes into theory of how strings are stored, not sure how relevant this is
# string chars are stored as numbers called code points, each having a special code per char
# this is stored in memory and decoded when accessing the string
# ' ' char or space is code point 32

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


# coding exercise - take string and find longest word, splitting on ' ', '\n', ',','.' 
sample_story = '''Once upon. a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

def get_longest_word(string):
    string_list = string.replace('.', ' ').replace(',', ' ').split() # replaces all necessary - splits on ' ', '\n'
    string_list = sorted(string_list, key=len, reverse=True) # good sort with nice custom params
    return string_list[0] # return top

print(get_longest_word(sample_story))


# comparison of strings
'Python' == 'Python' # True
'Python' == 'python' # False
'I love Python' < 'I love python' # tricky! python compares the 'P' to 'p', but the ASCII value
# in this case, 'P' is lower than 'p' (80 and 112, respectively), so evaluates True
'Pythonist' > 'Python' # only evaluates true because 'i' is greater than none
# > or < checks the ASCII value and compares
'P' > 'p' # false since 80 is not greater than 112
'Python' > 'p' # also false! since 'P' is less than 'p' -> length is not what is checked
# what the heck would we even use this for? I see no obvious use case
'20' > '8' # also false since '2' and '8' are being compared
'10' == 10 # false, since type is different
# 10 > '2' # TypeError since cannot compare different types

for i in ['a','b','c','d','e']:
    print(ord(i))

print(len('\n'))
print(len('\'\\'))


print('string'[::-1]) # this reverses the direction
print('string'[::4]) # selects every fourth char in a string

# can also use max('string') or min()
# this returns the char with the max or min code point value
print(max('david'))


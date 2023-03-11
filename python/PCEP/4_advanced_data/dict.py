
# dictionaries are collections of data used to store key/value pairs
# MUTABLE!

emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}

print(emails['Mark Steel'])
 # dictionaries must have unique keys, no dups allowed

# below will not work because keys are immutable, setting them in a list would make them mutable, and thus not work
#  ranking = {
#     [1]: 'fred',
#     [2]: 'steve',
#  }

# this dict object will work, strings are immutable
ranking = {
    1: 'fred',
    2: 'steve',
}

# operations!! (they are mutable!!)
grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)
grades['Anne'] = 'A'
print(grades)
grades.update({'John': 'A'})
print(grades)
# can update either by object replacement with .update or by value replacement, using square brackets
print(len(grades))

# this checks if the key is in grades
if 'John' in grades:
    print('Yay!')

# deletes the 'John' object
del grades['John']

# all of this is similar to lists!! 

# !! before python 3.6, dictionaries were not ordered
# now, dicts are ordered in 3.6

grades = {
    'John': 'A',
    'Anne': 'B',
    'George': 'D'
}

# only gets keys
for el in grades:
    print(el)

# only gets keys, this is the same as above, but different? not sure
for el in grades.keys():
    print(el)

# only gets values
for el in grades.values():
    print(el)

# this iterates dicts and can access both keys and values!
for person, grade in grades.items():
    print(person, 'got', grade)

# dict practice test!
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

# this will loop and ask the user for words until they respond with EXIT
while True:
    word = input('Enter a word in English or EXIT: ')
    if word == 'EXIT':
        print('Bye!')
        break
    else:
        if word in sample_dict:
            print('Translation:', sample_dict[word])
        else:
            print('No match!')

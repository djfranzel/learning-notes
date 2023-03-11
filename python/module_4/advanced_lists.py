
# swapping variables
first = input('first: ')
second = input('second: ')
print(first, second)
first, second = second, first
print(first, second)
# never seen this shorthand before, cool! 

# also used for lists!
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[-1] = top_cities[-1], top_cities[0]
print(top_cities)
top_cities.sort()
print(top_cities)

random_nums = [2, 5, 0, -3, 4]
random_nums.sort()
print(random_nums)
random_nums.sort(reverse=True) # will reverse the sort

# sometimes it is only necessary to temporarily sort a list
print(sorted(top_cities)) # this returns a sorted list, but does not mutate the original

# check presence in list!
invited_guests = ['Kate', 'Adam', 'Kerry']
name = input('What is your name? ')
if name in invited_guests:
    print('Yay!')
else:
    print('Sad!')

if name not in invited_guests:
    print('Sad!')
else:
    print('Yay!')

# important! this is a copy of the string value, not equating the reference
name_original = 'Jon Snow'
name_new = name_original

# different for complex data types! 
# these copy the reference and will update each other when modifying
list_original = [1, 2, 3]
list_new = list_original

# get around the reference copy by using slicing
list_new = list_original[:]
# this grabs a copy of the list and assigns it to the list_new variable

# way to create long list based on condensed loop
numbers = [i for i in range(1, 101)]
print(numbers)

# more advanced one
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)


# nested lists! 
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0][0]) # should print 'A1'

# nested loop results in printing all cells
for cell in cells:
    for item in cell:
        print(item)

# table format print, might be nice sometimes! 
for row in cells:
    for cell in row:
        print(cell, '', end='') # setting end to empty string removes default \n or newline char
    print() # this doesn't print anything, but adds the default \n for the end of each row


# nested lists with list populator shorthand
table = [[i for i in range(1, 6)] for j in range(4)]
print(table)

# multiplying lists!
list_us = ['NYC', 'Chicago']
list_uk = ['London', 'Bristol']
list_all = list_us + list_uk
print(list_all)

list_numbers = [0, 1] * 10
print(list_numbers)

# collections or container data types
# MUTABLE

# list! in python not an array, it is a list - I guess it probably doesn't matter that much
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)
print(top_cities[0])

# gets items counting from the end
print(top_cities[-1])
print(top_cities[-5])

# common pattern with range and slice, first number is inclusive, second is exclusive
# for 0 index, it includes this, for index 2 it goes until then and stops
print(top_cities[0:2]) # slice! 0 - 2 index
print(top_cities[2:]) # start at second index till end
print(top_cities[:3]) # start to 3rd item
print(top_cities[:]) # gets all, why extra syntax?
print(top_cities[10:15]) # doesn't error, but returns empty list, why no error!?

# deleting!
top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2] # deletes index 2 and shifts all items beyond one index back
print(top_cities)
del top_cities[3:] # deletes index 3 to the end
del top_cities[:] # this clears the list, but doesn't delete the variable
del top_cities # this deletes everything
# print(top_cities)

# adding new elements!
book_ratings = [7, 9, 5, 6, 8]
book_ratings.append(4) # adds to end of list
book_ratings.insert(1, 10) # adds number 10 at index 1 without deleting any items
print(book_ratings)

# iterating lists!
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
for city in top_cities:
    print('Current city:', city)

for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:', top_cities[city_index])

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Money spent:', sum)


# final exercise
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_count = 0
normal_count = 0
high_count = 0

for spend in spendings:
    if spend < 1000.0:
        low_count += 1
    elif spend >= 1000.0 and spend <= 2500.0:
        normal_count += 1
    else:
        high_count += 1

print('Numbers of months with low spendings: '+str(low_count)+', normal spendings: '+str(normal_count)+', high spendings: '+str(high_count)+'.')

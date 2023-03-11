
# similar to lists, but tuples are immutable!! 
# strings in python are also immutable, so changing requires new assignment/declaration

empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3
print(three_el_tuple)

one_el_tuple_a = 2,
print(one_el_tuple_a)

# can use len for tuples
user_data = ('John', 'American', 1964)
print(len(user_data))

for element in user_data:
    print(element)

# good example of how to concatenate and reassign tuple
user_data = user_data + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

## LISTS vs. TUPLES:
# lists are best when using items of same datatypes
# tuples are often used when using data of different types, but still related

# Lists in tuples and vice versa!
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = [city_1, city_2, city_3]

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])

# even though tuples are immutable, the list inside the tuple is STILL mutable, cool!
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.6)
print(user_data)

# test using iteration
connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

rome_flights = 0
total_time = 0

for connection in connections:
    if connection[1] == 'Rome':
        rome_flights += 1
        total_time += connection[2]

print(rome_flights, 'connections lead to Rome with an average flight time of', total_time / rome_flights,'minutes')


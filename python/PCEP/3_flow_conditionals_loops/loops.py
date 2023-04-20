
counter = 1 
while counter < 11:
    print(counter)
    counter += 1
print('Finished!')

print('''
==========================
=== SECRET NUMBER GAME ===
==========================
''')

secret_number = 14
user_input = int(input('Guess secret number between 0 - 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Guess secret number between 0 - 20: '))
print('Got it! ')

for letter in 'hello!':
    print(letter)

# worth pointing out that the start value is included, but stop is not
# at what point does it increment? probably before each iteration
for counter in range(1,11):
    print(counter)
print('finished!')

# default start value is zero
for counter in range(11):
    print(counter)
print('finished!')

# can also have a third which sets the increment
for counter in range(1, 11, 2):
    print(counter)
print('finished!')

# always runs until break hits
while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)

# if a number is divisible by 5, then we skip it using 'continue', otherwise print it
for counter in range(1,21):
    if counter % 5 == 0:
        continue
    print(counter)

# this just makes it so the code doesn't throw errors
for i in range(11):
    pass

# multiplication table with nested loop
for a in range(1,6):
    for b in range(1, 6):
        print(a, 'x', b, '=', a * b)

# this allows the loop to keep track of 'i' as it iterates
for i, num in enumerate([1,4,3,6]):
    print('i:', i)

# something with loops and else! this is new for me
# this is controversial in python
# only if there is a break will the else not execute
# looks more like a 'finally' or 'then' to me, but oh well
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)


# challenge at end
while True:
    guess = int(input('When was Python 1.0 released? '))
    if guess == 1994:
        print('Correct!')
        break
    elif guess > 1994:
        print('It was earlier than that!')
    elif guess < 1994:
        print('It was later than that!')
    
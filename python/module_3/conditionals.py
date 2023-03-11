
# use 4 spaces as standard for indentation

user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30')
    print('Sorry, you don\'t qualify' )
elif user_age == 30:
    print('you are 30')
else:
    print('You are 30 or younger')
    print('Congrats!')

if 2 == 2.0:
    print('true')

user_age = int(input('What is your age? '))
user_country = input('What is your country?')

if user_age < 25 and user_country == 'Germany':
    print('Yay!')
elif user_country == 'Germany' or user_country == 'USA':
    print('Yay! 2')
elif not user_country == 'Poland':
    print('Not! from poland')
elif not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
    print('conditions met!')
else:
    print('Nay!')

# use backslash to enable multi-line conditionals
# order of checking operations in python is 
# 1. not
# 2. and
# 3. or
# doesn't it just go left to right? I guess not, not totally clear on this
# video says to use brackets for clarity, seems like a good idea

days_ago = int(input('How many days ago have you purchased the item? '))
used = input('Have you used the item at all [y/n]? ')
broken = input('Has the item broken down on its own [y/n]? ')

success = 'You can get a refund.'
fail = 'You cannot get a refund.'

if days_ago <= 10 and used == 'n':
    print(success)
elif broken == 'y':
    print(success)
else:
    print(fail)
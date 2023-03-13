
import sys
import random

# generate a password based on user inputs

uppercase_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_set = 'abcdefghijklmnopqrstuvwxyz'
digits_set = '0123456789'
special_set = '!@#$%&*^|()_+'


def generate_password():
    length = int(input('Please provide password length: '))
    uppercase = input('Use uppercase letters? (y/n): ')
    digits = input('Use digits? (y/n): ')
    special_chars = input('Use special characters? (y/n): ')

    password = ''

    while len(password) < length:
        if uppercase == 'y':
            password += random.choice(uppercase_set)
        if digits == 'y' and len(password) < length:
            password += random.choice(lowercase_set)
        if special_chars == 'y' and len(password) < length:
            password += random.choice(special_set)
        if len(password) < length:
            password += random.choice(lowercase_set)
    else:
        print(password)

while True:

    choice = input('''-- Password generator --
Choose option:
1: generate password
2: exit the program
Your choice: ''')

    if choice == '1':
        generate_password()
        break
    elif choice == '2':
        print('Bye!')
        sys.exit()
    else:
        print('Please enter a correct value')




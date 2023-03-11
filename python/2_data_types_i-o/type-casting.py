height_cm = input('Height converter: enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48)
# can also simplify and remove second casted variable by casting the response of input

year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')

temp_c = input('Enter the temperature taday in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celcius equals ' + str(temp_f) + ' degrees Fahrenheit'
print(temp_statement)

# test
hours_worked = int(input('How many hours did you work last month? '))
hourly_rate = float(input('What is your hourly rate? '))

print('Last month, you earned', hours_worked * hourly_rate, 'dollars')

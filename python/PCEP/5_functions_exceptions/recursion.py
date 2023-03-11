
# recursion!!

# this is just using a loop, but recursion here might make this more consise
def get_factorial(number):
    factorial = 1
    for x in range(1, number +1):
        factorial *= x
    return factorial

print(get_factorial(6))

def get_factorial_recursion(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursion(number - 1)

print(get_factorial_recursion(6))

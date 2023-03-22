
# class variables are declared in the root class object, not in the __init__

class Dog():
    counter = 0 # this is shared across all instances of objects
    def __init__(self, name, age) -> None:
        self.__name = name
        self.age = age
        Dog.counter += 1

my_pet = Dog('Teddy', 2)
kates_pet = Dog('Foxy', 5)

print(my_pet.counter)
print(kates_pet.counter)
print(Dog.counter) # this is more clear since it really is the class that holds this var, not the instances of it

print(my_pet.__dict__) # does not show class variables, only instance variables

class Dog():
    __counter = 0 # this is shared across all instances of objects
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Dog.__counter += 1

print(Dog._Dog__counter) # will show the private counter with the name mangling
print(Dog.__dict__) # this shows all values on the class, not just the instance

my_pet = Dog('Tom', 4)

if hasattr(my_pet, 'name'): # this hasattr will check if the attribute exists
    print('yay')
else:
    print('nay')

if hasattr(Dog, '_Dog__counter'):
    print('yay')


print(Dog.__name__) # prints the actual name of the class
my_pet = Dog('Tom', 5)
print(type(my_pet).__name__) # also prints the name, just gets it from an instance of the class

print(Dog.__module__) # returns __main__ since the dog class exists in this file, not in a different module

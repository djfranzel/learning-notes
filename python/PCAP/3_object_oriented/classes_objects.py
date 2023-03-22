
# a class is a template used to create objects
# each class has a name, a set of properties, and a collection of methods

# this is a basic class, self is required and always use that syntax
class User:
    def __init__(self, nickname, city) -> None:
        self.nickname = nickname
        self.city = city

    def introduce(self):
        print('Hello, I am', self.nickname, 'and I live in', self.city)

# sample_user = User()
# sample_user.introduce()
# print(sample_user.nickname)

second_user = User('dave', 'mpls')
second_user.introduce()

# adding the initial_speed = 0 will set the default, so last argument is optional
# add __ before the variable to give it private status
# then it can't be mutated outside of the class itself
# this can help to add constraints on what values can be set
class Car():
    def __init__(self, model, color, initial_speed = 0) -> None:
        self.model = model
        self.color = color
        self.__speed = initial_speed
    
    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print('Current speed:', self.__speed)

my_lovely_car = Car('T-Roc', 'red', 5)
my_lovely_car.speed_up()
my_lovely_car.show_speed()
my_lovely_car.slow_down()
my_lovely_car.__speed = -20
my_lovely_car.show_speed()
print(my_lovely_car.__speed) # will show value, but you can't mutate a __ prefixed variable


# can add properties to classes even if they don't have them!

class Dog():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

my_pet = Dog('Teddy', 2)
my_pet.color = 'brown' # can add this property even though it's not initially in the object
del my_pet.name # now only two total props since name is deleted
print(my_pet.__dict__) # default method to list all props of the item!

# different objects of the same class can have different values
# is this weird? floppy? I guess there are uses, but differs from Java in this

class Dog():
    def __init__(self, name, age) -> None:
        self.__name = name
        self.age = age

my_pet = Dog('Teddy', 2)
print(my_pet.__dict__) # this is name mangling since __name is private, it gets a different key
print(my_pet._Dog__name) # this can actually access the prop! 

# thus the __ before a variable doesn't actually make it private, just makes it private by best practice
# name mangling doesn't work if you mutate the object outside the class, only when __ exists in the class
# all variables in the __init__ are instance variables

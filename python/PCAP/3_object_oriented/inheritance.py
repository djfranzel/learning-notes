
# inheritance is where one class can inherit values of other classes

class Vehicle:
    class_message = 'Message from vehicle'
    def __init__(self, speed) -> None:
        self.speed = speed

# this is python's syntax for subclass/class/inheriting props from previous
class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count) -> None:
        # Vehicle.__init__(self, speed)
        super().__init__(speed) # above is alternative, what is advantage? 
        self.wheel_count = wheel_count
        print(super().class_message)
    
    def speed_up(self):
        self.speed += 5

    def test_overriding(self):
        print('overriding in LandVehicle')

class Car(LandVehicle):
    def super_speed(self):
        print('Super speed activated!')
        super().speed_up()
        super().speed_up()
        super().speed_up()

    # when calling this from an instantiated Car object, this method will be used
    # not! the one in the LandVehicle class
    def test_overriding(self):
        print('overriding in Car')

# can check with below function
# is first arg a subclass of last arg, pretty logical
print(issubclass(Car, LandVehicle))
print(issubclass(Car, Vehicle)) # also True, even though one level removed
print(issubclass(Car, Car)) # also true, but no explanation given

my_car = Car(5, 4) # this is speed, and is removed up two levels of inheritance

print(my_car.__dict__)

print(my_car.class_message) # the class will inherit all previous instance and class variables

print(my_car.speed)
my_car.super_speed()
print(my_car.speed)
my_car.speed_up()
print(my_car.speed)

# overriding! 
# no special syntax, just redeclare the method or variable in the child class
# python goes up one by one and takes the first one that returns

print(my_car.test_overriding())

# when a child class calls a parent class method that calls a method that is overriden in the child class,
# the method in the child class actually is called
# this keeps everything consistent, so the most child level overriden method is always called

my_vehicle = Vehicle(60)
my_new_vehicle = my_vehicle # does not create a copy, simply points new to the memory location of my_vehicle
print(my_vehicle is my_new_vehicle) # 'is' checks whether the objects point to the same memory address
# '==' on the other hand checks equality of the objects

# more 'is' operations
first_num = 5
second_num = 5
print(first_num is second_num) # is true, but doesn't this check location, not value? 
# I guess there are some optimization in python that evaluates this as true, why?

first_str = 'hi'
second_str = 'hi'
print(first_str is second_str) # also true, as python optimizes this comparison

# BUT

first_str = 'hi'
second_str = 'h'
second_str += 'i'
print(first_str is second_str) # evaluates false

# is all of this because when the same variable value is instantiated, the 5 is actually stored 
# in the same place to reduce memory use, thus 'is' while comparing locations, evaluates true
# in the changed value, (+=) it allocates new space that doesn't share the same reference as the first,
# thus the 'is' operator does not share the location and evaluates False
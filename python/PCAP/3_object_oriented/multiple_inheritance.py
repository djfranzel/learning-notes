
# multiple inheritance

class Vehicle():
    def go(self):
        print('Going!')

    def introduce(self):
        print('Hi, Vehicle!')

class Flyable():
    def flying(self):
        print('Flying!')

    def introduce(self):
        print('Hi, Flyable!')

class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()
my_plane.go()
my_plane.flying()
my_plane.introduce() # MRO - method resolution order
# will print from Vehicle value since it appears first in the inherited arguments

# sometimes these inherited conflicts get complicated, so really try to avoid it
# use single inheritance and only double when you really need it, probably not common

print(Airplane.__bases__) # returns all the 'base' objects used to create that object
print(Vehicle.__bases__) # just returns the object reference
print(Vehicle)

# diamond problem

class Vehicle():
    def power_type(self):
        print('Various power types')

class ElectricVehicle(Vehicle):
    def power_type(self):
        print('Electric power')

class PetrolVehicle(Vehicle):
    def power_type(self):
        print('Petrol power')

class HybridVehicle(ElectricVehicle, PetrolVehicle):
    pass

hybrid_vehicle = HybridVehicle()
hybrid_vehicle.power_type()

# different languages have different solutions for this problem
# python uses its MRO, so this outputs the first argument's value - electric
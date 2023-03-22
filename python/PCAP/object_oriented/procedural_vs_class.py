
# procedural programming is below, and has disadvantages

def calculat_area(width, height):
    return width * height

width = int(input('Width? '))
height = int(input('Height? '))
area = calculat_area(width, height)
print('Area:', area)

# this above is just step by step evaluating code procedurally

# below is a class that defines the object, provides a constructor and returns a useful computation
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
a = int(input('Width? '))
b = int(input('Height? '))
rectangle = Rectangle(a, b)
print('Area:', rectangle.get_area())

# using OOP techniques, complex data is organized and structured
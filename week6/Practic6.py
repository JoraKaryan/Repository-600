
import math
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        if not isinstance(radius, int):
            raise Exception("Please type an integer")
        if not isinstance(radius, int):
            raise Exception("Please type a string")
        print( "{1} circle with radius {0}".format(radius, color))

    def area(self):
        return math.pi * (self.radius)**2

    def circumference(self):
        return 2 * math.pi * self.radius



    def __add__(self):
        
        if obj1.circumference() >= obj.circumference():
            return obj1.circumference() - obj.circumference()
        else:
            obj.circumference() - obj1.circumference()

obj = Circle(155, "red")
obj1 = Circle(204, "yellow")
print (obj1.circumference())
print(obj1.__add__())



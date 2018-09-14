# from math import pi
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi*self.radius**2, 3)

    def circumferance(self):
        return round(2*math.pi*self.radius)

    @classmethod
    def unit_cirlce(cls):
        print(cls)
        return cls(1)


if __name__ =="__main__":
    c = Circle(5)
    b = c.unit_cirlce()
    print(b.radius, b.area())
    # u = Circle(1)
    unit = Circle.unit_cirlce()
    print(unit.radius, unit.area())
    print("Area of Circcle: {}".format(c.area()), "Circumferance \
    of Circle: {}".format(c.circumferance()))

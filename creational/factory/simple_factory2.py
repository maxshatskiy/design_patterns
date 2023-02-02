"""simple factory as defined in Eckel B."""

from __future__ import generators
import random
class Shape(object):

    @staticmethod
    def factory(type):
        if type == "Circle": return Circle()
        if tpye == "Square": return Square()
        assert 0, "Bad shape creation: " + type

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [Shape.factory(i) for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()
import math

class Geometric: # superklass
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def area(self):
        pass
    
    @property
    def perimeter(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def is_inside(self, point_x, point_y):
        pass
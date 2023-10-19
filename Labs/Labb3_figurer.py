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
        if isinstance(other, Rectangle):
            return self.area < other.area
        return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.area > other.area
        return False

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

class Rectangle(Geometric):                      # underklass
    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def is_square(self):
        return self.side1 == self.side2

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.x, self.y, self.side1, self.side2) == (other.x, other.y, other.side1, other.side2)
        return False
    
    
    def is_inside(self, point_x, point_y):
        half_width = self.side1 / 2
        half_height = self.side2 / 2
        x_min = self.x - half_width
        x_max = self.x + half_width
        y_min = self.y - half_height
        y_max = self.y + half_height
        return x_min <= point_x <= x_max and y_min <= point_y <= y_max


class Circle(Geometric): #underklass
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_unit_circle(self):
        return self.radius == 1

    def __eq__(self, other):
        if isinstance(other, Circle):
            return (self.x, self.y, self.radius) == (other.x, other.y, other.radius)
        return False
        
    def is_inside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.x) ** 2 + (point_y - self.y) ** 2)
        return distance <= self.radius
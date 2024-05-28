import math

def TriangleCondition(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a + b <= c or a + c <= b or b + c <= a:
        return 2

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side must be non-negative")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle:
    def __init__(self, a, b, c):
        if TriangleCondition(a, b, c) == 1:
            raise ValueError("Sides must be non-negative")
        elif TriangleCondition(a, b, c) == 2:
            raise ValueError("Triangle inequality not met")
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))
    def perimeter(self):
        return self.a + self.b + self.c



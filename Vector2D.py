import math
from random import random


class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def __pow__(self, scalar):
        return Vector2D(self.x ** scalar, self.y ** scalar)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def get_length(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def set_length(self, length):
        old_length = self.get_length()
        self.x *= length/old_length
        self.y *= length/old_length
        return self

    def dot_product(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def normalized(self):
        length = self.get_length()

        if length != 1:
            return Vector2D(self.x / length, self.y / length)
        else:
            return Vector2D(self.x, self.y)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_sqrd(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    @staticmethod
    def zero():
        return Vector2D(0, 0)

    @staticmethod
    def one():
        return Vector2D(1, 1)

    @staticmethod
    def random(scale=1):
        return Vector2D(
            random()*scale,
            random()*scale)

    @staticmethod
    def up():
        return Vector2D(0, 1)

    @staticmethod
    def down():
        return Vector2D(0, -1)

    @staticmethod
    def left():
        return Vector2D(-1, 0)

    @staticmethod
    def right():
        return Vector2D(1, 0)

    @staticmethod
    def inner_sum(vector: "Vector2D"):
        return vector.x + vector.y



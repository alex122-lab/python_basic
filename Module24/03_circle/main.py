import math

class Сircle:
    num_pi = math.pi
    def __init__(self, x = 0, y = 0, r = 1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return self.num_pi * self.r ** 2

    def perimeter(self):
        return 2 * self.num_pi * self.r

    def scale(self, k):
        self.r *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2

def intersection(Сircle_1, Сircle_2):
    if Сircle_1.is_intersect(Сircle_2):
        print('Круги пересекаются')
    else:
        print('Круги не пересекаются')

Unit_1 = Сircle(0,0,1)
Unit_2 = Сircle(3,0,1)

print(Unit_1.square())
print(Unit_1.perimeter())

intersection(Unit_1, Unit_2)

print()
Unit_1.scale(10)
print(Unit_1.square())
print(Unit_1.perimeter())

intersection(Unit_1, Unit_2)





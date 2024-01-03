import math

class MyMath:
    """
     класс `MyMath`, состоящий из следующих методов
     - вычисление длины окружности,
    - вычисление площади окружности,
    - вычисление объёма куба,
    - вычисление площади поверхности сферы.
     """

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """метод, позволяющий конвертировать строку даты в объект класса `Date`,
        состоящий из соответствующих числовых значений дня, месяца и года"""
        result = 2 * math.pi * radius
        return result

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """метод, вычисляющий площадь окружности"""
        result = math.pi * radius ** 2
        return result

    @classmethod
    def cube_value(cls, edge: float) -> float:
        """метод, вычисляющий объем куба"""
        result = edge ** 3
        return result

    @classmethod
    def sphere_area(cls, radius: float) -> float:
        """метод, вычисляющий площадь поверхности сферы"""
        result = 4 * math.pi * radius ** 2
        return result

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_value(edge=7.2)
res_4 = MyMath.sphere_area(radius=8.1)

print(res_1)
print(res_2)
print(res_3)
print(res_4)

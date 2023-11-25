class Iterator:
    """Итератор последовательности из N элементов"""
    def __init__(self, num):
        self.__num = num
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__num:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration

def square_gen(num):
    """Генератор последовательности из N чисел"""
    for elem in range(1,num + 1):
        yield elem ** 2

square_gen_exp = (num ** 2 for num in range(1,11))
"""Генераторное выражение"""

my_iter = Iterator(num=10)
for elem in my_iter:
    print(elem, end=' ')
print('\n')

for elem in square_gen(num=10):
    print(elem, end=" ")
print('\n')

for elem in square_gen_exp:
    print(elem, end=" ")

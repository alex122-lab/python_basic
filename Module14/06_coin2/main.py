# TODO здесь писать код
def my_find(x, y, radius):
    if -radius <= x <= radius and -radius <= y <= radius:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')

print('Введите координаты монетки')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

my_find(x, y, radius)
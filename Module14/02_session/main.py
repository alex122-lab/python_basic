print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))

print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
print("Уравнение прямой, проходящей через эти точки:")
if x1 - x2 == 0:
    print('x = ', x2)
elif y1 - y2 == 0:
    print('y = ', y2)
else:
    x_diff = x1 - x2
    y_diff = y1 - y2
    k = y_diff / x_diff
    b = y2 - k * x2
    print("y = ", k, " * x + ", b)

# зачёт!

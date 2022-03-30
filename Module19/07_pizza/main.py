# вариант № 1
def fun(dct, key, arg):
    dct[key] = dct.setdefault(key, 0) + int(arg)
    return dct


d = {}
for i in range(int(input('Введите кол-во заказов: '))):
    fio, pizza, amount = input(f'{i + 1} заказ: ').rsplit(maxsplit=3)
    d[fio] = fun(d.get(fio, {}), pizza, amount)

for name in sorted(d):
    print(f'{name}:')
    for pizza, amount in sorted(d.get(name).items()):
        print(f'{pizza}: {amount}')
    print()
# вариант № 2
d = {}
for i in range(int(input('Введите кол-во заказов: '))):
    fio, pizza, amount = input(f'{i + 1} заказ: ').rsplit(maxsplit=3)
    dct = d.get(fio, {})
    dct[pizza] = dct.setdefault(pizza, 0) + int(amount)
    d[fio] = dct
    dct = {}
for name in sorted(d):
    print(f'{name}:')
    for pizza, amount in sorted(d.get(name).items()):
        print(f'{pizza}: {amount}')
    print()

# вариант № 3
count = int(input('Введите кол-во заказов: '))
orders = {}
for i in range(1, count + 1):
    order = input(f'{i} заказ: ').split()
    fio_pizza = ' '.join(order[:2])
    count = ' '.join(order[2])
    orders[fio_pizza] = orders.setdefault(fio_pizza, 0) + int(count)

next_fio = ''
for fio_pizza in sorted(orders):
    fio = fio_pizza.split()[0]
    pizza = fio_pizza.split()[1]
    if next_fio != fio:
        print(fio, ':')
    print('   ', pizza, ':', orders[fio_pizza])
    next_fio = fio

# зачёт!

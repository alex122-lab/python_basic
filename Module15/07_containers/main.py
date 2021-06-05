def number(mass):
    while True:
        if not mass.isdigit() or not int(mass) < 200:
            mass = input('Ошибка ввода, введите целое число < 200 кг: ')
        else:
            return mass

count = int(input('Кол-во контейнеров: '))
containers = []
for _ in range(1, count + 1):
    mass_container = number(input('Введите вес контейнера: '))
    containers.append(mass_container)

new_mass_container = int(number(input('\nВведите вес нового контейнера: ')))
num = 1
for mass in containers:
    if new_mass_container <= int(mass):
        num += 1

print('\nНомер, куда встанет новый контейнер:', num)

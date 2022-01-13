list_1 = []
list_2 = []
for i in range(3):
    print('Введите', i + 1, 'число для первого списка: ')
    num_1 = int(input())
    list_1.append(num_1)
for i in range(7):
    print('Введите', i + 1, 'число для второго списка: ')
    num_2 = int(input())
    list_2.append(num_2)
print('Первый список: ', list_1)
print('Второй список: ', list_2)
list_1.extend(list_2)
list_1 = list(set(list_1))
print('Новый первый список с уникальными элементами: ', list_1)


def shift(list_start):
    K = int(input('Сдвиг: '))
    print('Изначальный список: ', list_start)
    for i in range(K):
        list_start.insert(0, list_start.pop(len(list_start) - 1))
    return print('Сдвинутый список: ', list_start,'\n')

list_start = [1, 2, 3, 4, 5]
shift(list_start)
list_start = [1, 4, -3, 0, 10]
shift(list_start)



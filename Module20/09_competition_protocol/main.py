def fun(dct, surname):
    dct.append(surname)
    return dct

dct_record = {}
for i in range(int(input('Сколько записей вносится в протокол? '))):
    result, surname = input(f'запись {i + 1}: ').rsplit(maxsplit=2)
    result = int(result)
    dct_record[result] = fun(dct_record.get(result, []), surname)
print('Итоги соревнований: ')

i = 0
list_surname = []
for result, surnames in sorted(dct_record.items(), reverse=True):
    for name in surnames:
        if len(list_surname) > 2:
            break
        elif name not in list_surname:
            i += 1
            print(f'{i} место. {name}', '(', result, ')')
            list_surname.append(name)

count_men = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек')
list_men = list(range(1, count_men + 1))
out = 0
for _ in range(count_men - 1):
    print('Текущий круг людей:', list_men)
    start_count = out % len(list_men)
    out = (start_count + number - 1) % len(list_men)
    print('Начало счёта с номера', list_men[start_count])
    print('Выбывает человек под номером', list_men[out])
    list_men.remove(list_men[out])

print('Остался человек под номером', list_men)

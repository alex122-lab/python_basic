list_a = [1, 5, 3]
list_b = [1, 5, 1, 5]
list_c = [1, 3, 1, 5, 3, 3]

list_a.extend(list_b)
num_5 = list_a.count(5)

for _ in range(num_5):
    list_a.remove(5)
list_a.extend(list_c)
num_3 = list_a.count(3)

print('Кол-во цифр 5 при первом объединении:', num_5)
print('Кол-во цифр 3 при втором объединении:', num_3)
print('Итоговый список:', list_a)

# зачёт!

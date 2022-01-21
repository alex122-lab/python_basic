list_1 = list(range(160, 177, 2))
list_2 = list(range(162, 181, 3))
list_1.extend(list_2)
list_1 = list(set(list_1))
print('Отсортированный список учеников:', list_1)

# зачёт!

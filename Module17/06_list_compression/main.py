import random

N = int(input('Кол-во чисел в списке: '))
list_start = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия:', list_start[:])
for i in range(list_start.count(0)):
    list_start.remove(0)
    list_start.append(0)
list_end = [list_start[num] for num in range(len(list_start)) if list_start[num] != 0]
print('Список после сжатия:', list_end)

# зачёт!

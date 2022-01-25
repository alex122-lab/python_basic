import random
sticks = int(input('Кол-во палок: '))
thows = int(input('Кол-во бросков: '))
list_stick = [1 for _ in range(sticks)]

for _ in range(thows):
    list_throw = [random.randint(0, 1) if list_stick[num] == 1 else 0 for num in range(sticks)]
    list_stick = [list_stick[num] if list_throw[num] == 0 else 0 for num in range(sticks)]
list_end = ['I' if list_stick[num] == 1 else '.' for num in range(sticks)]
new_list_end = ''
for i_num in list_end:
    new_list_end += i_num
print('Результат: ', new_list_end)
# print('Результат: ', *list_end, sep = "")


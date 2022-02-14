text_1 = input('Первая строка: ')
text_2 = input('Вторая строка: ')
flag = False
step = -1
for _ in range(len(text_1)):
    step += 1
    text_step = text_2[-step:] + text_2[:-step]
    if text_step == text_1:
        flag = True
        break
# TODO, Предлагаю убрать из решения переменную флаг и добавить блок else в цикл for.
#  Если из цикла при помощи break не вышли, отработает блок else цикла for.
#  Немного подробней, про блоки else циклов for и while, можно почитать тут
#  https://habr.com/ru/post/148365/

if flag:
    print('Первая строка получается из второй со сдвигом', step, '.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

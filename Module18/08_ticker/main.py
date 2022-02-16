text_1 = input('Первая строка: ')
text_2 = input('Вторая строка: ')
step = -1
for _ in range(len(text_1)):
    step += 1
    text_step = text_2[-step:] + text_2[:-step]
    if text_step == text_1:
        print('Первая строка получается из второй со сдвигом', step, '.')
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

# зачёт!

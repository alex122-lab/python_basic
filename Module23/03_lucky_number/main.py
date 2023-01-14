import random

num_sum = 0
try:
    while num_sum < 777:
        num = int(input('Введите число: '))
        num_sum += num
        x = random.randint(1, 13)
        if x == 6:
            raise BaseException
        else:
            with open('out_file.txt', 'a') as out_file:
                out_file.write(str(num) + '\n')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')

except BaseException:
    print('Вас постигла неудача!')
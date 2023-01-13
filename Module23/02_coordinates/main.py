import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

text = ''
num_str = 0
try:
    file = open('coordinates.txt', 'r', encoding='utf-8')
    for line in file:
        num_str += 1
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            try:
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                my_list = sorted([res1, res2, number])
                my_list = map(str, my_list)
                text += (' '.join(my_list)) + '\n'

            except ZeroDivisionError:
                print("Деление на '0' во второй функции")
            except ValueError:
                print('Некорректные данные в строке', num_str, 'файла coordinates.txt')

        except ZeroDivisionError:
            print("Деление на '0' в первой функции")
        except ValueError:
            print('Некорректные данные в строке', num_str, 'файла coordinates.txt')

    file.close()
    file_2 = open('result.txt', 'w')
    file_2.write(text)
    file_2.close()

except FileNotFoundError:
    print('Файл coordinates.txt не найден.')
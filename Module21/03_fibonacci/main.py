def fib(num_pos):
    if num_pos == 1 or num_pos == 2:
        return 1
    else:
        sum_num = fib(num_pos - 1) + fib(num_pos - 2)
        return sum_num
num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fib(num_pos))
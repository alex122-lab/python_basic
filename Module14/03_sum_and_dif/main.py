def my_sum(num):
    sum_num = 0
    for i in num:
        sum_num += int(i)
    return sum_num


def my_count(num):
    count_num = len(num)
    return count_num


num = input('Введите число: ')

sum_num = my_sum(num)
count_num = my_count(num)

print('Сумма цифр: ', sum_num)
print('Кол-во цифр в числе: ', count_num)
print('Разность суммы и кол-ва цифр: ', sum_num - count_num)

# зачёт!

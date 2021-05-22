def my_sum(num):
    sum_num = 0
    for i in num:
        sum_num += int(i)
    return sum_num

def my_count(num):
    count_num = len(num)
    return count_num


num = input('Введите число: ')
print('Сумма цифр: ', my_sum(num))
print('Кол-во цифр в числе: ', my_count(num))
print('Разность суммы и кол-ва цифр: ', my_sum(num) - my_count(num))



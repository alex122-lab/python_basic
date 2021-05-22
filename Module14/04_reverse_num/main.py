def my_revers(num):
    whole_part = ''
    fractional_part = ''
    flag = True
    for i in num:
        if i != '.' and flag:
            whole_part = i + whole_part
        elif i == '.':
            flag = False
        else:
            fractional_part = i + fractional_part
    rev_num = whole_part + '.' + fractional_part
    return rev_num

num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')

print('Первое число наоборот: ', my_revers(num1))
print('Второе число наоборот: ', my_revers(num2))
print('Сумма: ', float(my_revers(num1)) + float(my_revers(num2)))




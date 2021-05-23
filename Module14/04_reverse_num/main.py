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

rev_num1 = my_revers(num1)
rev_num2 = my_revers(num2)

print('Первое число наоборот: ', rev_num1)
print('Второе число наоборот: ', rev_num2)
print('Сумма: ', float(rev_num1) + float(rev_num2))

# зачёт!

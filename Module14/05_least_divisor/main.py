def my_divide(num):
    min_divide = num
    for i in range(2, num + 1):
        if num % i == 0 and i < min_divide:
            min_divide = i
    return min_divide


num = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы: ', my_divide(num))

# зачёт!

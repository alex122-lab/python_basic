def calculating_math_func(data):
    result = 1
    list_len = len(list_fact)
    if data < list_len:
        result = list_fact[data-1]
    else:
        result = list_fact[list_len-1]
        for index in range(list_len+1, data + 1):
            result *= index
            list_fact.append(result)
    result /= data ** 3
    result = result ** 10
    return result

list_fact = [1]
data_fact = 1
while True:
    data_fact = int(input('Введите число: '))
    result_fact = calculating_math_func(data_fact)
    print(result_fact)




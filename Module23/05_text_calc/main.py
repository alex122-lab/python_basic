def num_field(line, num): # функция проверки количество полей
    if len(line) == num:
        return True

def range_num(num): # функция проверки целых чисел
    if str(num).isdigit():
        if type(int(num) == int):
            return True

def range_operationis(operation): # функция проверки арифметических операций
    list_operationis = ['+', '-', '/', '//', '%', '*', '**']
    if operation in list_operationis:
        return True

def dict_operationis(num_1, num_2, operation): # функция проведения арифметических операций
    dict_operations = {'+': int(num_1) + int(num_2), '-': int(num_1) - int(num_2), '/': int(num_1) / int(num_2),
                       '//': int(num_1) // int(num_2), '%': int(num_1) % int(num_2), '*': int(num_1) + int(num_2),
                       '**': int(num_1) ** int(num_2)}
    if operation in dict_operations.keys():
        result = dict_operations[operation]
        return result

sum_num = 0
with open('calc.txt', 'r') as calc:
    for i_line in calc:
        list_field = i_line.split()
        ask = ''
        while not ask == 'нет':
            try:
                if num_field(list_field, 3):
                    num_1, oper, num_2 = list_field
                    if not range_num(num_1) or not range_num(num_2):
                        raise ValueError
                    elif not range_operationis(oper):
                        raise SyntaxError
                    else:
                        result = dict_operationis(num_1, num_2, oper)
                        sum_num += result
                        ask = 'нет'
                else:
                    raise IndexError
            except (IndexError, ValueError, SyntaxError):
                ask = input(f'Обнаружена ошибка в строке: {i_line[:-1]}   Хотите исправить? ').lower()
                if ask == 'да':
                    answer = input('Введите исправленную строку: ')
                    list_field = answer.split()

print('Сумма результатов:', sum_num)
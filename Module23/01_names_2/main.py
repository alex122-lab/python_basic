line_count = 0
sym_sum = 0

try:
    with open('people.txt', 'r') as people_file:
        for i_line in people_file:
            try:
                line_count += 1
                length = len(i_line)
                if i_line.endswith('\n'):
                    length -= 1
                sym_sum += length
                if length < 3:
                    raise ValueError
            except ValueError:
                print('Ошибка: менее трёх символов в строке {}.'.format(line_count))
                with open('errors.log', 'a') as error_file:
                    error_file.write(i_line)
except FileNotFoundError:
    print ('Файл не найден.')
finally:
    print('Общее количество символов: ', sym_sum)

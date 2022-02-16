file_name = input('Название файла: ')
simbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
for _ in range(1):  # TODO, цикл for получился лишним, т.к. всегда состоит из одной итерации.
    if file_name.startswith(simbols):
        print('Ошибка: название начинается на один из специальных символов')
    if not file_name.endswith(('.txt', '.docx')):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    else:
        print('Файл назван верно.')

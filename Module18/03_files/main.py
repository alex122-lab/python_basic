file_name = input('Название файла: ')
simbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
flag = True
if file_name.startswith(simbols):
    print('Ошибка: название начинается на один из специальных символов')
    flag = False
if not file_name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    flag = False

if flag:
    print('Файл назван верно.')

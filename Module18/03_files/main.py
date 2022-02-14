file_name = input('Название файла: ')
simbols = ('@', '№', '$', '%', '^', '&', '*', '(', ')')
flag = True
if file_name.startswith(simbols):
    print('Ошибка: название начинается на один из специальных символов')
    flag = False
if not file_name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
    flag = False
# TODO, Предлагаю убрать из решения переменную флаг и добавить блок else в цикл for.
#  Если из цикла при помощи break не вышли, отработает блок else цикла for.
#  Немного подробней, про блоки else циклов for и while, можно почитать тут
#  https://habr.com/ru/post/148365/

if flag:
    print('Файл назван верно.')

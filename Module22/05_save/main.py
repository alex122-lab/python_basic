import os

def write_file(file_n, text_w, massage='Файл успешно сохранён!'):
    text_file = open(file_n, 'w', encoding='utf-8')
    text_file.write(text_w)
    print(massage)
    text_file.close()

text = input('Введите строку: ')
path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
path_for_save = os.path.abspath(os.path.join(os.path.sep, *path))

if os.path.isdir(path_for_save):
    file_name = input('Введите имя файла: ') + '.txt'
    file_save = os.path.join(path_for_save, file_name)
    if os.path.isfile(file_save):
        ask = input('Вы действительно хотите перезаписать файл? ').lower()
        if ask == 'да':
            write_file(file_save, text, 'Файл успешно перезаписан!')
    else:
        write_file(file_save, text)
else:
    print('Ошибка ввода, такой директории не существует')


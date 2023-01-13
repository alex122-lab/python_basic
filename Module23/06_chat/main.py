def write_file(name_file, text, action):  # функция записи в файл
    nf = name_file[:-4]
    with open(name_file, action) as nf:
        nf.write(text)


name_user = input('Введите имя пользователя: ')
while True:
    ask = input(
        'Выберите действие: посмотреть текущий текст чата - Ч / отправить сообщение - П,  выйти из программы - любой символ: ').lower()
    if ask == 'ч':
        try:
            with open('chat.txt', 'r') as rf:
                data = rf.read()
                print(data)
        except FileNotFoundError:
            print('Слежебное сообщение: пока ничего нет')
    elif ask == 'п':
        message = input('Введите текст сообщения: ')
        message = name_user + ':   ' + message + '\n'
        write_file('chat.txt', message, 'a')
    else:
        break

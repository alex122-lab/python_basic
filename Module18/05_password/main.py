
# TODO, переменная alphabet получилась лишней. Чтобы проверить, является ли символ буквой,
#  стоит использовать метод строк isalpha().

  # TODO, эту переменную стоит создавать внутри цикла while.
while True:
    flag = True
    password = input('Придумайте пароль: ')
    len_p = len(password)
    count_up_letter = 0
    count_d = 0
    for letter in password:
        if not letter.isalpha() and not letter.isdigit():
            flag = False
        elif letter.isupper():
            count_up_letter += 1
        elif letter.isdigit():
            count_d += 1
    if flag and len_p >= 8 and count_up_letter >= 1 and count_d >= 3:
        print('Файл назван верно.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')


def move(n, x=1, y=2):
    if n == 1:
        print(111, f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
    else:
        move(n - 1, x, 6 - x - y)
        print(222, f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n - 1, 6 - x - y, y)


number = int(input('Введите количество дисков: '))
move(number)

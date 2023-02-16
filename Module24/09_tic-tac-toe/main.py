class Cell:
    status = ' '  # - занята она или нет

    def __init__(self, number):
        self.number = number #   - номер клетки

class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.numbers = [Cell(number) for number in range(1, 10)]

    def info_board(self):
        for cell in self.numbers[0:3]:
            print(f' {cell.number}({cell.status}) ', end='')
        print('\n')
        for cell in self.numbers[3:6]:
            print(f' {cell.number}({cell.status}) ', end='')
        print('\n')
        for cell in self.numbers[6:9]:
            print(f' {cell.number}({cell.status}) ', end='')
        print('\n ---------------')

    def control_victory(self):
        if self.numbers[0].status == self.numbers[1].status== self.numbers[2].status !=' ' \
                or self.numbers[3].status == self.numbers[4].status == self.numbers[5].status !=' '\
                or self.numbers[6].status == self.numbers[7].status == self.numbers[8].status !=' '\
                or self.numbers[0].status == self.numbers[3].status == self.numbers[6].status !=' '\
                or self.numbers[1].status == self.numbers[4].status == self.numbers[7].status !=' '\
                or self.numbers[2].status == self.numbers[5].status == self.numbers[8].status !=' '\
                or self.numbers[0].status == self.numbers[4].status == self.numbers[8].status !=' '\
                or self.numbers[2].status == self.numbers[4].status == self.numbers[6].status !=' ':
            return True
        else:
            return False

class Player:
    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    def __init__(self,name, board,sign):
        self.name = name #  - имя
        self.board = board
        self.sign = sign


    def step_cell(self,num_cell):
        if self.board.numbers[num_cell - 1].status == ' ' :
            self.board.numbers[num_cell - 1].status = self.sign #  на какую клетку ходит
        else:
            print('Ошибка ввода - клетка занята, попробуйте еще раз')
            num = int(input(f'Выберите другую клетку для хода: '))
            self.step_cell(num)


board = Board()
name_1 = input('Введите имя первого игрока: ')
player_1 = Player(name_1, board, 'x')
name_2 = input('Введите имя второго игрока: ')
player_2 = Player(name_2, board, '0')

board.info_board()
count = 0
while True:
    num = int(input(f'Укажите номер клетки на которую ходит игрок {name_1} символом х: '))
    player_1.step_cell(num)
    board.info_board()
    count += 1
    if board.control_victory():
        print(f'В игре победил игрок {name_1}')
        break
    elif count == 5:
        print('Ничья')
        break
    num = int(input(f'Укажите номер клетки на которую ходи игрок {name_2} символом 0: '))
    player_2.step_cell(num)
    board.info_board()
    if board.control_victory():
        print(f'В игре победил игрок {name_2}')
        break

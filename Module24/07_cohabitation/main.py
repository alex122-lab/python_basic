import random
class Fridge:

    def __init__(self):
        self.food = 50

class Bedside_table:

    def __init__(self):
        self.money = 0

class House:
    def __init__(self, fridge, bedside_table):
        self.fridge = fridge
        self.bedside_table = bedside_table
    def house_info(self):
        print(f'В холодильнике продуктов на {self.fridge.food} руб., '
              f'денег в тумбочке - {self.bedside_table.money} руб.\n')

class Person:

    def __init__(self, name, house):
        self.name = name # имя
        self.satiety = 50 # степень сытости
        self.house = house # дом

    def person_info(self): # человек
        if self.satiety <= 0:
            print(f'Человек {self.name} умер от голода\n')
        else:
            print(f'Человек - {self.name}, степень сытости - {self.satiety}\n')

    def eat(self): # ест
        count_food = self.house.fridge.food
        if count_food == 0:
            print(f'В холодильнике нет еды')
            self.go_for_food()
        else:
            if count_food > 10:
                self.house.fridge.food -= 10
                self.satiety += 10
            else:
                self.house.fridge.food -= count_food
                self.satiety += count_food
            print(
                f'Человек {self.name} поел, '
                f'в холодильнике еды - {self.house.fridge.food}, '
                f'денег - {self.house.bedside_table.money} руб., '
                f'степень сытости - {self.satiety}')

    def work(self): # работает
        self.satiety -= 10
        if self.satiety <= 0:
            print(f'Человек {self.name} умер от голода во время работы\n')
            return False
        self.house.bedside_table.money += 25
        print(f'{self.name} поработал, '
              f'денег стало {self.house.bedside_table.money} руб., '
              f'в холодильнике еды - {self.house.fridge.food}, '
              f'степень сытости - {self.satiety}')

    def game(self): # играет
        self.satiety -= 5
        if self.satiety <= 0:
            print(f'Человек {self.name} умер от голода во время игры\n')
            return False
        print(f'{self.name} поиграл, '
              f'денег - {self.house.bedside_table.money} руб., '
              f'в холодильнике еды - {self.house.fridge.food}, '
              f'степень сытости - {self.satiety}')

    def go_for_food(self): # ходит в магазин за едой
        count_money = self.house.bedside_table.money
        if count_money >= 15:
            self.house.bedside_table.money -= 15
            self.house.fridge.food += 15
        elif 0 < count_money < 15:
            self.house.bedside_table.money -= count_money
            self.house.fridge.food += count_money

        print(f'{self.name} сходил в магазин за едой, '
              f'денег осталось - {self.house.bedside_table.money} руб., '
              f'в холодильнике еды - {self.house.fridge.food}, '
              f'степень сытости - {self.satiety}')

fridge = Fridge()
bedside_table = Bedside_table()
house_1 = House(fridge, bedside_table)
human_1 = Person('Сидоров Иван', house_1)
human_2 = Person('Петров Максим', house_1)
human_1.person_info()
human_2.person_info()


num_day = 0
while num_day <= 365 and (human_1.satiety > 0 or human_1.satiety > 0):
    num_day += 1
    # 1. Генерируется число кубика от 1 до 6.
    number = random.randint(1,6)
    # 1. Если сытость < 20, то поесть.
    if human_1.satiety < 20:
        human_1.eat()
    elif human_2.satiety < 20:
        human_2.eat()
    # 1. Иначе, если еды в доме < 10, то сходить в магазин.
    elif house_1.fridge.food < 10 and human_1.satiety < 20:
        human_1.go_for_food()
    elif house_1.fridge.food < 10 and human_2.satiety < 20:
        human_2.go_for_food()
    # 1. Иначе, если денег в доме < 50, то работать.
    elif house_1.bedside_table.money < 50:
        human_1.work()
    # 1. Иначе, если кубик равен 1, то работать.
    elif number == 1:
        human_1.work()
    # 1. Иначе, если кубик равен 2, то поесть.
    elif number == 2:
        human_1.eat()
        human_2.eat()

    # 1. Иначе играть.
    else:
        human_1.game()
        human_2.game()
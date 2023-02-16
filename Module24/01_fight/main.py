import random

class Unit:
    warrior_name = ' Tom'
    warrior_health = 100
    is_life = True

    def print_info(self):
        print(
            'name: {}\nhealth: {}\nlife_status: {}'.format(
                self.warrior_name, self.warrior_health, self.is_life))

    def attack(self):
        self.warrior_health -= 20

Unit_1 = Unit()
Unit_2 = Unit()
Unit_1.warrior_name = 'Джеймс'
Unit_2.warrior_name = 'Билли'

while Unit_1.warrior_health > 0 and Unit_2.warrior_health > 0:
    result = random.randint(1, 2)
    if result == 2:
        Unit_1.attack()
        print(f'Атаковал {Unit_2.warrior_name} - '
              f'у {Unit_1.warrior_name} осталось здоровья {Unit_1.warrior_health}')
        name_Victor = Unit_2.warrior_name
    else:
        Unit_2.attack()
        print(f'Атаковал {Unit_1.warrior_name} - '
              f'у {Unit_2.warrior_name} осталось здоровья {Unit_2.warrior_health}')
        name_Victor = Unit_1.warrior_name

print(f'Победу одержал {name_Victor}')



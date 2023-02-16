class Parent:

    def __init__(self, full_name, age, list_kids):
        self.full_name = full_name
        self.age = age
        self.list_kids = list_kids

    def parent_info(self):
        print(
            'Родитель: {}, возраст: {}, дети: {}'.format(
                self.full_name, self.age, self.list_kids))
    def calm(selfs, num_kid):
        num_kid.calm_state = 1

    def hungry(selfs, num_kid):
        num_kid.hungry_state = 1

class Kid:
    calm_states = {1: 'спокоен ', 0: 'плачет '}
    hungry_states = {1: 'сыт ', 0: 'голоден '}

    def __init__(self, name_kid, age_kid):
        self.name_kid = name_kid
        self.age_kid = age_kid
        self.calm_state = 0
        self.hungry_state = 0

    def kid_info(self):
        print(f'Ребенок {self.name_kid}, возраст {self.age_kid} лет, '
              f'{Kid.hungry_states[self.calm_state]} и {Kid.calm_states[self.hungry_state]}')

def control_age(num_parent, list_kid):
    for num_kid in list_kid:
        if num_parent.age - num_kid.age_kid < 16:
            print(f'Разница в возрасте родителя {num_parent.full_name} и ребенка {num_kid.name_kid} менее 16 лет')
            num_kid.age_kid = int(input(f'Введите правильный возраст ребенка {num_kid.name_kid}: '))
            num_parent.age = int(input(f'Введите правильный возраст родителя {num_parent.full_name}: '))
            control_age(num_parent, [num_kid])
        else:
            num_parent.list_kids.append([num_kid.name_kid, num_kid.age_kid])

kid_1 = Kid('Кирилл', 8)
kid_2 = Kid('Марина', 5)

parent_1 = Parent('Сидоров Алексей Михайлович', 42, [])
control_age(parent_1, [kid_1, kid_2])

parent_2 = Parent('Сидорова Маргарита Анатольевна', 38, [])
control_age(parent_2, [kid_1, kid_2])

parent_1.parent_info() # Информация о родителе
parent_2.parent_info() # Информация о родителе

kid_1.kid_info() # Информация о ребенке
parent_1.calm(kid_1)
parent_1.hungry(kid_1)
kid_1.kid_info() # Информация о ребенке

kid_2.kid_info() # Информация о ребенке
parent_2.calm(kid_2)
parent_2.hungry(kid_2)
kid_2.kid_info() # Информация о ребенке
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
come = ()
while come != 'пора спать':
    number = len(guests)
    print('Сейчас на вечеринке', number, ' человек:',  guests)
    come = input('Гость пришел или ушел? ')

    if come == 'пришел' and number <= 5:
        name = input('Имя гостя: ')
        # TODO, если гость уже есть в списке, то не добавляем. Иначе, задвоим гостей.
        #  Наличие элемента в списке, стоит проверять при помощи оператора вхождения "in". Пример:
        #  if 1 in [1, 2, 3]:
        #      print('Есть!')
        guests.append(name)
        print('Привет', name, '!')
    elif come == 'ушел' and number > 0:
        name = input('Имя гостя: ')
        # TODO, если гостя в списке нет, то не удаляем. Иначе, получим ошибку.
        guests.remove(name)
    elif come == 'пришел' and number > 5:
        print('Гостей не может быть больше 6')
    elif come == 'ушел' and number == 0:
        print('Гостей нет')





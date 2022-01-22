guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
come = ()
while come != 'пора спать':
    number = len(guests)
    print('Сейчас на вечеринке', number, ' человек:',  guests)
    come = input('Гость пришел или ушел? ')

    if come == 'пришел' and number <= 5:
        name = input('Имя гостя: ')
        if not name in guests:
            guests.append(name)
            print('Привет', name, '!\n')
    elif come == 'ушел' and number > 0:
        name = input('Имя гостя: ')
        print('Пока', name, '!\n')
        if name in guests:
            guests.remove(name)
    elif come == 'пришел' and number > 5:
        print('Прости', name, 'но мест нет')
print('\nВечеринка закончилась, все легли спать.')





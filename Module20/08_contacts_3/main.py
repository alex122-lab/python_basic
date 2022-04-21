dict_tel = {}
while True:
    action_num = int(input('Введите номер действия:\n 1. Добавить контакт \n 2. Найти человека \n'))
    if action_num == 1:
        name_surname = tuple(input('Введите имя и фамилию нового контакта(через пробел): ').split())
        for name_sur in dict_tel:
            if name_sur == name_surname:
                print('Такой человек уже есть в контактах.')
                print('Текущий словарь контактов:', dict_tel)
                break
        else:
            num_tel = int(input('Введите номер телефона: '))
            dict_tel.update({name_surname : num_tel})
            print('Текущий словарь контактов:', dict_tel)
    elif action_num == 2:
        surname = input('Введите фамилию для поиска: ')
        for fam, age in dict_tel.items():
            if fam[1].lower() == surname.lower():
                print(fam[0], fam[1], age)
    else:
        print('Введен неправильный номер действия!')


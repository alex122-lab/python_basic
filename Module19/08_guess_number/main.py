number_max = int(input('Введите максимальное число: '))
number_set = {num for num in range(1, number_max + 1)}
boris_phrase = ''
boris_numbers_set = set()
while len(boris_numbers_set) != 1:
    boris_phrase = input('Нужное число есть среди вот этих чисел: ')
    if boris_phrase == 'Помогите!':
        print('Артём мог загадать следующие числа: ',' '.join(map(str, number_set)))
        break
    else:
        boris_numbers = boris_phrase.split()
        boris_numbers_set = set(map(int, boris_numbers))
        print(boris_numbers_set)
        artems_answer = input('Ответ Артёма: ')
        if artems_answer == 'Да':
            number_set = number_set & boris_numbers_set
        elif artems_answer == 'Нет':
            number_set -= boris_numbers_set
else:
    if artems_answer == 'Нет':
        print('Борис проиграл')
    else:
        print('Борис выиграл')
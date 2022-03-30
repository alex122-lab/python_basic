number_max = int(input('Введите максимальное число: '))
numbers_dict = {str(num_dict): 'Нет' for num_dict in range(1, number_max + 1)}

while True:
    boris_phrase = input('Нужное число есть среди вот этих чисел: ')
    if boris_phrase == 'Помогите!':
        print('Артём мог загадать следующие числа: ', end='')
        for number, word in numbers_dict.items():
            if word == 'Да':
                print(number, end=' ')
        break
    else:
        # TODO, списки, словари и циклы for в текущем задании лишние.
        #  Стоит работать с множествами. Небольшая шпаргалка по операциям над множествами:
        #  https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
        boris_phrase = boris_phrase.split()
        artems_answer = input('Ответ Артёма: ')
        for num in numbers_dict:
            if num in boris_phrase:
                numbers_dict[num] = artems_answer

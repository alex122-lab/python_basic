word_vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
list_sentence = input('Введите текст: ')
list_vowels = [letter for letter in list_sentence if letter in word_vowels]
print('\nСписок гласных букв', list_vowels)
print('Длина списка', len(list_vowels))

# зачёт!

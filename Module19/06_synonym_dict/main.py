orders = dict()
count = int(input('Введите количество пар слов: '))
words = {}
for i in range(1, count + 1):
    two_words = input(f'{i} пара: ').lower().split(' - ')
    words.update({two_words[0]:two_words[1], two_words[1]:two_words[0]})

new_word = ''
while new_word not in words:
    new_word = input('Введите слово: ').lower()
    if new_word in words:
        print('Синоним:', words[new_word])
    else:
        print('Такого слова в словаре нет.')

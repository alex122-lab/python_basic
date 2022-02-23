orders = dict()
count = int(input('Введите кол-во заказов: '))
for i in range(1, count + 1):
    two_words = input(f'{i} пара: ').split(' - ')
    words.update({two_words[0]:two_words[1]})

new_word = input('Введите слово: ').lower()
for word, synonym in words.items():
    if new_word == word.lower():
        print('Синоним:', synonym)
        break
    elif new_word == synonym.lower():
        print('Синоним:', word)
        break
else:
    print('Такого слова в словаре нет.')
word = input('Введите слово: ')
# count = 0
unique = 0
for letter in word:
    count = 0
    for letter_word in word:
        if letter == letter_word:
            count += 1
    if count < 2:
        unique += 1
print('Кол-во уникальных букв: ', unique)

# зачёт!

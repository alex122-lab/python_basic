word = input('Введите слово: ')
count = 0
unique = 0
for letter in word:
    if letter not in word[0:count] and letter not in word[count + 1:]:
        unique += 1
    count += 1

print('Кол-во уникальных букв: ', int(unique))

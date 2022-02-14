text = input('Введите строку: ').split()
text.sort(key=len, reverse=True)
max_word = text[0]
max_len_word = len(max_word)
print('Самое длинное слово:', max_word)
print('Длина этого слова:', max_len_word)

# 2 решение
# text = input('Введите строку: ').split()
# list_len_word = [len(word) for word in text]
# max_len_word = max(list_len_word)
# index_max_word = list_len_word.index(max_len_word)
# max_word = text[index_max_word]
# print('Самое длинное слово:', max_word)
# print('Длина этого слова:', max_len_word)

# зачёт!

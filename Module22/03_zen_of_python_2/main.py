import os
def lat_letter(symbol):
    LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if symbol in LETTERS:
        return True

def eng_word(word):
    for sym in word:
        if lat_letter(sym):
            return True

path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
speakers_file = open(path, 'r', encoding='utf-8')

lines = 0
words = 0
symbols = 0
dict_letters = {}
for str_line in speakers_file:
    lines += 1
    for sym in str_line:
        if lat_letter(sym):
            symbols += 1
            sym = sym.lower()
            dict_letters[sym] = dict_letters.setdefault(sym, 0) + 1
    for sym in str_line.split():
        if eng_word(sym):
            words += 1
rare_k = [rare_k for rare_k, v in dict_letters.items() if v == min(dict_letters.values())][0]

speakers_file.close()

print('Количество букв в файле: ', symbols)
print('Количество слов в файле: ', words)
print('Количество строк в файле: ', lines)
print('Наиболее редкая буква: ', rare_k)

# # 2 вариант - Наиболее редкая буква:
# from collections import Counter
# counter = Counter(dict_letters)
# rare_l = min(counter, key=counter.get)
# print('Наиболее редкая буква: ', rare_l)

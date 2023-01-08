def lat_letter(symbol):
    LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if symbol in LETTERS:
        return True
def write_file(file_n, text_w):
    text_file = open(file_n, 'w', encoding='utf-8')
    text_file.write(text_w)
    text_file.close()

speakers_file = open('text.txt', 'r', encoding='utf-8')

symbols = 0
dict_letters = {}

for str_line in speakers_file:
    for sym in str_line:
        if lat_letter(sym):
            symbols += 1
            sym = sym.lower()
            dict_letters[sym] = dict_letters.setdefault(sym, 0) + 1

speakers_file.close()

sorted_key = dict(sorted(dict_letters.items(), key=lambda x: x[0]))
sorted_value = sorted(sorted_key.items(), key=lambda x: x[1], reverse=True)

text = ''
for letter in sorted_value:
    text += letter[0] + ' ' + '{:0.3f}'.format(letter[1]/symbols) + '\n'

write_file('analysis.txt', text)
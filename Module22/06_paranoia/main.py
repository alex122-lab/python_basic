import os

def lat_letter(symbol):
    LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if symbol in LETTERS:
        return True

def code_caesar(letter, step):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    if letter in letters:
        letter_step = letters[(letters.index(letter) + step + 52) % 52]
        return letter_step

def write_file(file_n, text_w):
    text_file = open(file_n, 'w', encoding='utf-8')
    text_file.write(text_w)
    text_file.close()

speakers_file = open('text.txt', 'r', encoding='utf-8')

step = 0
str_code = ''
for str_line in speakers_file:
    step += 1
    for sym in str_line:
        if lat_letter(sym):
            code_sym = code_caesar(sym, step)
            str_code += code_sym
        else:
            str_code += sym
write_file('cipher_text.txt', str_code)








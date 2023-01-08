import zipfile
archive = 'voyna-i-mir.zip'

directory_to_extract_to = 'war_and_peace'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall(directory_to_extract_to)

def write_file(file_n, text_w):
    text_file = open(file_n, 'w', encoding='utf-8')
    text_file.write(text_w)
    text_file.close()

speakers_file = open('war_and_peace/voyna-i-mir.txt', 'r', encoding='utf-8')

symbols = 0
dict_letters = {}

for str_line in speakers_file:
    for sym in str_line:
        if sym.isalpha():
            symbols += 1
            sym = sym.lower()
            dict_letters[sym] = dict_letters.setdefault(sym, 0) + 1

speakers_file.close()

sorted_key = dict(sorted(dict_letters.items(), key=lambda x: x[0]))
sorted_value = sorted(sorted_key.items(), key=lambda x: x[1], reverse=True)

text = ''
for letter in sorted_value:
    text += letter[0] + ' ' + '{:8.6f}'.format(letter[1]/symbols) + '\n'

write_file('analysis.txt', text)
print(text)

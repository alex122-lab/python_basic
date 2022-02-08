text = input('Введите строку: ')
cnt = 0
code_text = ''
for i in range(len(text)):
    sym = text[i]
    cnt += 1
    if i == len(text) - 1:
        code_text = code_text + text[i] + str(cnt)
        break
    if text[i] != text[i + 1]:
        code_text = code_text + sym + str(cnt)
        cnt = 0
print('Закодированная строка:', code_text)

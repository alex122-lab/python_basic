text = input('Сообщение: ')
new_text = []
start = 0
for i, sym in enumerate(text):
    if not sym.isalpha():
        new_text.insert(i, sym)
        start = i + 1
    else:
        new_text.insert(start, sym)

print('Новое сообщение:', ''.join(new_text))

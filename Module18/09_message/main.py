text = input('Сообщение: ')
# TODO, переменная alphabet получилась лишней. Чтобы проверить, является ли символ буквой,
#  стоит использовать метод строк isalpha().
r_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
new_text = []
start = 0
for i, sym in enumerate(text):
    if sym not in r_alphabet:
        new_text.insert(i, sym)
        start = i + 1
    else:
        new_text.insert(start, sym)

print('Новое сообщение:', ''.join(new_text))

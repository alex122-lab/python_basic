alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
chift = int(input('Введите сдвиг: '))
code = [(alphabet[(alphabet.index(sym) + chift) % 33] if sym != ' ' else ' ') for sym in text]
new_code = ''
for i_num in code:
    new_code += i_num
print(new_code)

print('Зашифрованное сообщение:', new_code)
# or i in message:
#         mesto = alfavit_RU.find(i)   # Алгоритм для шифрования сообщения на русском
#         new_mesto = mesto + smeshenie
#         if i in alfavit_RU:
#             itog += alfavit_RU[new_mesto]
#         else:
#             itog += i
# TODO здесь писать код

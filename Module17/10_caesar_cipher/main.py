def caesar_code(input_text, input_shift):
    code = [(alphabet[(alphabet.index(sym) + input_shift) % 33] if sym != ' ' else ' ') for sym in input_text]
    new_code = ''
    for i_num in code:
        new_code += i_num
    return new_code


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
output_code = caesar_code(text, shift)
print('Зашифрованное сообщение:', output_code)

# зачёт!

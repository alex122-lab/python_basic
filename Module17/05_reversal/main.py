text = input('Введите строку: ')
first_index = text.index('h')
reverse_text = text[::-1]
end_index = len(text) - reverse_text.index('h') - 1
result = text[end_index - 1:first_index:-1]
print('Развернутая последовательность между первым и последним h: ', result)

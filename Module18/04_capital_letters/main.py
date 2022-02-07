text = input('Введите строку: ').split()
result = [word.title() for word in text]
print(' '.join(result))
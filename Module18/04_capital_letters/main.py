text = input('Введите строку: ').split()
result = [word.title() for word in text]
print(' '.join(result))

# TODO, пожалуйста, обратите внимание, при использовании метода .title() цикл for получился лишним.
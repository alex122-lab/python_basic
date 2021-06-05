def revers_word(word):
    count = len(word)
    for i in range(count // 2):
        if word[i] != word[count - i - 1]:
            result = 'Слово не является палиндромом'
            return result
        else:
            result = 'Слово является палиндромом'
            return result


word = input('Введите слово: ')
print(revers_word(word))

# зачёт!

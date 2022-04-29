def shorted_range(lst, tpl):
    return min(len(lst), len(tpl))
str_letter = 'abcd'
tuple_number = (10, 20, 30, 40)

pairs = ((str_letter[i_elem], tuple_number[i_elem]) for i_elem in range(shorted_range(str_letter, tuple_number)))
print(('Результат: '))
print(pairs)
for i_elem in pairs:
    print(i_elem)
print()
zipped = zip(str_letter,tuple_number)
print(zipped)
print(list(zipped))


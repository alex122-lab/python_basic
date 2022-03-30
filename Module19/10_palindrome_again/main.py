str_in = input('Введите строку: ')
dict_sym = {}

for sym in str_in:
    dict_sym[sym] = dict_sym.setdefault(sym, 0) + 1

sym_honest = 0
sym_count = len(dict_sym)

# TODO, Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" не отражает. В нашем случае, "i" это не Индекс.
for i in dict_sym.values():
    if i % 2 != 0:
        sym_honest += 1
if sym_honest > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

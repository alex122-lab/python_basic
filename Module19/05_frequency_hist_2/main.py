text = input('Введите текст: ')
dict_hist = {sym:text.count(sym) for sym in set(text)}
print('Оригинальный словарь частот: ')
for sym, count in sorted(dict_hist.items()):
    print(sym, ':', count)

dict_hist_inv = {count:[] for count in dict_hist.values()}
for sym, count in dict_hist.items():
    dict_hist_inv[count].append(sym)

print('Инвертированный словарь частот: ')
for count, sym in dict_hist_inv.items():
    print(count, ':', sym)


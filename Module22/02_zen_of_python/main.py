speakers_file = open('zen.txt', 'r', encoding='utf-8')
sym_count = []
for i_line in speakers_file:
    sym_count.append(i_line)
sym_count[len(sym_count)-1] += '\n'
speakers_file.close()

print('\n',end=''.join(sym_count[::-1]))


# 2 вариант:
# for i_line in sym_count[::-1]:
#     print(i_line, end='')


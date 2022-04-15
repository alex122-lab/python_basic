def borders(list_num, num):
    if list_num.count(num) == 0:
        border_beg = 0
        border_fin = 0
    elif list_num.count(num) == 1:
        border_beg = list_num.index(num)
        border_fin = len(list_num) + 1
    else:
        border_beg = list_num.index(num)
        border_fin = list_num.index(num, border_beg + 1) + 1
    list_num_border = (i for i in range(border_beg, border_fin))
    return list_num_border

def slicer(list_num, num):
    return tuple(sym for i, sym in enumerate(list_num) if i in borders(list_num, num))

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 10))

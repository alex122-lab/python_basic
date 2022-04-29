def tpl_sort(*tpl):
    corted_list = sorted(tpl)
    return tuple(corted_list)

print(tpl_sort(6, 3, -1, 8, 4, 10, -5))
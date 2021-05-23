def year_num(year1, year2):
    for year in range(year1, year2 + 1):
        num_1 = year // 1000 % 10
        num_2 = year // 100 % 10
        num_3 = year // 10 % 10
        num_4 = year % 10
        # TODO, возможно, для улучшения читаемости кода,
        #  не стоит делать такие большие условия в одном блоке, но создать несколько блоков elif.
        if (num_1 == num_2 == num_3 != num_4) or (num_2 == num_3 == num_4 != num_1) \
                or (num_1 == num_3 == num_4 != num_2) or (num_1 == num_2 == num_4 != num_3):
            print(year)

year1 = int(input('Ведите первый год: '))
year2 = int(input('Ведите второй год: '))

print('Года от ', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
year_num(year1, year2)

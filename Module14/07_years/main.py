def year_num(year1, year2):
    for year in range(year1, year2 + 1):
        for i in set(str(year)):
            if str(year).count(i) == 3:
                print(year)

    # TODO, отличное решение! =)
    #  Предлагаю пока что решить без метода count.
    #  Так же стоит попробовать решить без вложенного цикла, т.к. циклы создают нагрузку на код.
    #  Возможно сможем реализовать обычный условный оператор?


year1 = int(input('Ведите первый год: '))
year2 = int(input('Ведите второй год: '))

print('Года от ', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
year_num(year1, year2)

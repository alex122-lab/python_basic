def year_num(year1, year2):
    for year in range(year1, year2 + 1):
        for i in set(str(year)):
            if str(year).count(i) == 3:
                print(year)

year1 = int(input('Ведите первый год: '))
year2 = int(input('Ведите второй год: '))

print('Года от ', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
year_num(year1, year2)




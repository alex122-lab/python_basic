def year_num(year1, year2):
    for year in range(year1, year2 + 1):
        if len(set(str(year))) == 2 and len(set(str(year)[0:2])) != len(set(str(year)[2:])):
            print(year)

year1 = int(input('Ведите первый год: '))
year2 = int(input('Ведите второй год: '))

print('Года от ', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
year_num(year1, year2)

city_country = dict()
count_country = int(input('Кол-во стран: '))
for i in range(1, count_country + 1):
    print(i, 'страна: ')
    country_city_title = input().split()
    city_country.update({country_city_title[0]:country_city_title[1:]})

for i in range(1, 4):
    title = input(f'{i} город: ')
    for country in city_country:
        # TODO, цикл for ниже получился лишним. Наличие ключа в словаре можно проверить при помощи оператора вхождения "in".
        for city in city_country[country]:
            if title == city:
                print('Город', city, 'расположен в стране', country, '.')
else:  # TODO, блок else будет выполнен всегда, т.к. в цикле for отсутствует break.
    print('По городу', title, 'данных нет.')


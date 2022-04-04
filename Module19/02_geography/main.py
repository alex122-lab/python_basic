city_country = dict()
count_country = int(input('Кол-во стран: '))
for i in range(1, count_country + 1):
    print(i, 'страна: ')
    country_city_title = input().split()
    city_country.update({country_city_title[0]:country_city_title[1:]})
print(city_country)
for i in range(1, 4):
    city = input(f'{i} город: ')
    for country in city_country:
        if city in city_country[country]:
            print('Город', city, 'расположен в стране', country, '.')
            break
    else:
        print('По городу', city, 'данных нет.')


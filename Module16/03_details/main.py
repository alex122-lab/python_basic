shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count_detail = 0
cost = 0
name = input('Название детали: ')
for i_detail in shop:
    if i_detail[0] == name:
        count_detail += 1
        cost += i_detail[1]
print('Кол-во деталей -', count_detail)
print('Общая стоимость -', cost)

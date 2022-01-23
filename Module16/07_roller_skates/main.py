list_skates = []
list_men = []
count = 0

count_skates = int(input('Кол-во коньков: '))
for i in range(1, count_skates + 1):
    print('Размер', i, 'пары: ')
    size = int(input())
    list_skates.append(size)
list_skates = sorted(list_skates)
count_men = int(input('Кол-во людей: '))

for i in range(1, count_men + 1):
    print('Размер ноги', i, 'человека: ')
    foot = int(input())
    list_men.append(foot)
list_men = sorted(list_men)
for foot in list_men:
    for skate in list_skates:
        if foot <= skate:
            list_men.remove(foot)
            list_skates.remove(skate)
            count += 1
            break

print('Наибольшее кол-во людей, которые могут взять ролики:', count)

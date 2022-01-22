list_skates = []
list_men = []
count = 0

count_skates = int(input('Кол-во коньков: '))
for i in range(1, count_skates + 1):
    print('Размер', i + 1, 'пары: ')  # TODO +1 в этой строке кода получилось лишним.
    size = int(input())
    list_skates.append(size)
list_skates = sorted(list_skates)
count_men = int(input('Кол-во людей: '))

# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
#  В таком случае, вычисление произойдёт только 1 раз в range, вместо вычислений каждую итерацию цикла.
for i in range(count_men):
    print('Размер ноги', i + 1, 'человека: ')
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

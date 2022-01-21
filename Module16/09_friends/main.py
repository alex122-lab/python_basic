N = int(input('Кол-во друзей: '))
N_kredit = int(input('Долговых расписок: '))
list_friends = []
number = 0

# TODO, предлагаю упростить реализацию. Создать список [0, 0, 0], в котором элемент — это сумма долга, а его позиция, это номер друга.
#  И работать только с этим списком.
for i in range(N):
    list_friends.append(list(range(2)))
    list_friends[i][0] = i + 1
    list_friends[i][1] = 0

for i in range(N_kredit):
    number += 1
    print(number,'расписка')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    if to_who != from_who:
        how_much = int(input('Сколько: '))
        list_friends[to_who - 1][1] -= how_much
        list_friends[from_who - 1][1] += how_much
    else:
        print('Самому себе нельзя давать в долг')

print('\nБаланс друзей:')
for i in range(N):
    print(list_friends[i][0], ':',list_friends[i][1] )
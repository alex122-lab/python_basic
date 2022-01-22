N = int(input('Кол-во друзей: '))
N_kredit = int(input('Долговых расписок: '))
list_friends = []
number = 0

for i in range(N):
    list_friends.append(0)

for i in range(N_kredit):
    number += 1
    print(number,'расписка')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    if to_who != from_who:
        how_much = int(input('Сколько: '))
        list_friends[to_who - 1] -= how_much
        list_friends[from_who - 1] += how_much
        print(list_friends)
    else:
        print('Самому себе нельзя давать в долг')

print('\nБаланс друзей:')
for i in range(N):
    print(i + 1, ':',list_friends[i])

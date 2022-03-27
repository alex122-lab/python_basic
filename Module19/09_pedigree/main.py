# TODO здесь писать код
def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])


p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)


d = {}
for i in range(int(input('Введите кол-во человек: '))):
    name_baby, name_father = input(f'{i + 1} пара: ').rsplit(maxsplit=2)
    dct = d.get(name_father, {})
    print(dct)
    dct[name_father] = name_baby
    print(dct)

   d[name_father] =  dct
    print(d)
    dct = {}
for name in sorted(d):
    print(f'{name}:')
    for pizza, amount in sorted(d.get(name).items()):
        print(f'{pizza}: {amount}')
    print()

# Введите количество человек: 9
# 1 пара: Alexei Peter_I
# 2 пара: Anna Peter_I
# 3 пара: Elizabeth Peter_I
# 4 пара: Peter_II Alexei
# 5 пара: Peter_III Anna
# 6 пара: Paul_I Peter_III
# 7 пара: Alexander_I Paul_I
# 8 пара: Nicholaus_I Paul_I
# вариант 1
def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])


p_tree = {}
# n = int(input())
# for i in range(n - 1):
#     child, parent = input().split()
#     p_tree[child] = parent
count_men = int(input('Введите количество человек: '))
for i in range(1, count_men + 1):
    child, parent = input(f'{i} пара: ').split()
    p_tree[child] = parent
heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

print()
print('“Высота” каждого члена семьи: ')
for key, value in sorted(heights.items()):
    print(key, value)

# вариант 2
# count_men = int(input('Введите количество человек: '))
# p_tree = {}
# for i in range(1, count_men + 1):
#     child, parent = input(f'{i} пара: ').split()
#     p_tree[child] = parent
# heights = {}
# for man in set(p_tree.keys()).union(set(p_tree.values())):
#     if man not in p_tree:
#         heights[man] = 0
#     else:
#         man_p = man
#         while man_p in p_tree:
#             heights[man] = heights.setdefault(man, 0) + 1
#             man_p = p_tree[man_p]
# print()
# print('“Высота” каждого члена семьи: ')
# for name, count in sorted(heights.items()):
#     print(name, count)

# зачёт!

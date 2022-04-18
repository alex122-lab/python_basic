original_list = [num for num in range(10)]
new_list = []
# 1) способ
for i in range(0, len(original_list), 2):
    pair_num = i, i + 1
    new_list.append(pair_num)

print(new_list)
# 2) способ
new_list = [(i, i + 1) for i in range(0, len(original_list), 2)]
print(new_list)

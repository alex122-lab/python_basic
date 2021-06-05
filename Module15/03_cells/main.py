count = int(input('Кол-во клеток: '))
cells = []
for i in range(1, count + 1):
    efficiency = int(input(f'Эффективность {i} клетки: '))
    if efficiency < i:
        cells.append(efficiency)
        new_cells = list(map(str, cells))
        output = ' '.join(new_cells)
print('Неподходящие значения:', output)

# зачёт!

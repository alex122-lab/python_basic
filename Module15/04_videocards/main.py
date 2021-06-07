count = int(input('Кол-во видеокарт: '))
graphics_card = []
max = 0
for _ in range(1, count + 1):
    number = int(input('Видеокарта: '))
    graphics_card.append(number)
    if number > max:
        max = number
new_graphics_card = graphics_card.copy()
for i in graphics_card:
    if i == max:
        new_graphics_card.remove(max)

print('Старый список видеокарт: ', graphics_card)
print('Новый список видеокарт: ', new_graphics_card)

# зачёт!

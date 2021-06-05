count = int(input('Кол-во видеокарт: '))
graphics_card = []
for _ in range(1, count + 1):
    number = int(input('Видеокарта: '))
    graphics_card.append(number)

new_graphics_card = graphics_card.copy()
for num in new_graphics_card:
    if num == max(new_graphics_card):
        new_graphics_card.remove(num)

print('Старый список видеокарт: ', graphics_card)
print('Новый список видеокарт: ', new_graphics_card)

# TODO, предлагаю пока что решить без функции max,
#  возможно, мы сможем определить наибольший номер видеокарты в первом цикле? =)

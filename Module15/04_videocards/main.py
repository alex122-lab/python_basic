count = int(input('Кол-во видеокарт: '))
graphics_card = []
for _ in range(1, count + 1):
    number = int(input('Видеокарта: '))
    graphics_card.append(number)

new_graphics_card = graphics_card.copy()
max = graphics_card[0]
for num in new_graphics_card:
    if num > max:
        max = num

# TODO, таким образом, мы удаляем только один элемент списка.
#  Стоит попробовать определить максимальное значение элемента в цикле с запросом ввода пользователя.
#  Во втором цикле, стоит ввести проверку и добавить только те элементы, которые меньше максимального. =)
new_graphics_card.remove(max)

print('Старый список видеокарт: ', graphics_card)
print('Новый список видеокарт: ', new_graphics_card)

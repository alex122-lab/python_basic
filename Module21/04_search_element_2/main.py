site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def key_find(struct, key, delth):
	if key in struct:
		result = struct[key]
		return result
	if delth > 1:
		for sub_struct in struct.values():
			if isinstance(sub_struct, dict):
				result = key_find(sub_struct,key,delth-1)
				if result:
					break
		else:
			result = None
		return result

user_key = input('Введите искомый ключ: ')
delth_y = input('Хотите ввести максимальную глубину? Y/N: ')
while delth_y not in ('Y','y','N','n'):
	delth_y = input('Ошибка ввода! Хотите ввести максимальную глубину? Y/N: ')
if delth_y == 'N' or delth_y == 'n':
	value = key_find(site, user_key, 2)
else:
	delth_max = int(input('Введите максимальную глубину: '))
	value = key_find(site, user_key, delth_max)

print('Значение ключа:', value)



























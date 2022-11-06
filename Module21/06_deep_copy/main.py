site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iphone',
			'div': 'Купить',
			'p': 'продать'
		}
	}
}

def key_find(struct, key,maining):
	if key in struct:
		struct[key] = maining
		result = struct[key]
		return result
	for sub_struct in struct.values():
		if isinstance(sub_struct, dict):
			result = key_find(sub_struct,key,maining)
			if result:
				return result


site_num = int(input('Введите количество сайтов '))
for _ in range(site_num):
	phone_name = input('Введите название телефона: ')
	key_phone = {'title' : f'Куплю/продам {phone_name} недорого', 'h2' : f'У нас самая низкая цена на {phone_name}'}
	for i in key_phone:
		key_find(site, i, key_phone[i])

	print(f'сайт для {phone_name}:')
	print(site,'\n')

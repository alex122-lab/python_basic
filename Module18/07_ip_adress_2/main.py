ip_ad = input('Введите IP: ').split('.')
if len(ip_ad) != 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for num in ip_ad:
        if not num.isnumeric():
            print(num, '- не целое число')
            break
        elif int(num) > 255:
            print(num, 'превышает 255')
            break
    else:
        print('IP-адрес корректен')

# зачёт!

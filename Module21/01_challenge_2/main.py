def numbers(number, count):
    if count < number:
        count += 1
        print(count)
        return numbers(number, count)

count = 0
num = int(input('Введите num: '))
numbers(num, count)

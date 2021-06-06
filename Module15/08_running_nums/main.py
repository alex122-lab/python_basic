def shift(nums):
    K = int(input('\nСдвиг: '))
    print('Изначальный список:', nums)
    delta = len(nums)
    for _ in range(K):
        for i in range(delta - 1, 0, -1):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return print('Отсортированный список:', nums)

list_start = [1, 2, 3, 4, 5]
shift(list_start)
list_start = [1, 4, -3, 0, 10]
shift(list_start)


def sort(my_list):
    print('Изначальный список:', my_list)
    my_list = sorted(my_list)
    print('Отсортированный список:', my_list)


my_list = [1, 4, -3, 0, 10]
sort(my_list)


def bubble_sort(nums):
    swapped = True
    print('\nИзначальный список:', nums)
    # TODO Предлагаю попробовать заменить цикл while на for.
    #  Дело в том, что цикл for будет работать быстрее, т.к. формирует условие для своей работы только 1 раз, при создании.
    #  В то время, как цикл while проверяет условие своей работы каждую итерацию цикла.
    #  В таком случае, первый цикл for получится исходя из длины списка =)
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return print('Отсортированный список:', nums)


bubble_sort(my_list)

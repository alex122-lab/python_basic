def sort(my_list):
    print('Изначальный список:', my_list)
    my_list = sorted(my_list)
    print('Отсортированный список:', my_list)


my_list = [1, 4, -3, 0, 10]
sort(my_list)


def bubble_sort(nums):
    print('\nИзначальный список:', nums)
    for _ in range(len(nums)):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return print('Отсортированный список:', nums)

bubble_sort(my_list)

def sort(my_list):
    print('Изначальный список:', my_list)
    my_list = sorted(my_list)
    print('Отсортированный список:', my_list)

my_list = [1, 4, -3, 0, 10]
sort(my_list)



def bubble_sort(nums):
    swapped = True
    print('\nИзначальный список:', nums)
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return print('Отсортированный список:', nums)

bubble_sort(my_list)
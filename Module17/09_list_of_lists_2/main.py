nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

list_number = [num_3 for num_1 in nice_list for num_2 in num_1 for num_3 in num_2]
print(list_number)


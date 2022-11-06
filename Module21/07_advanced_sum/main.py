def sum_struct(struct):
	for sub_struct in struct:
		if type(sub_struct) == int:
			sum_out[0] += sub_struct
		else:
			sum_struct(sub_struct)
	return sum_out

in_list = (1, 2, 3, 4, 5)
sum_out = [0]
sum_struct(in_list)
print(sum_out[0])
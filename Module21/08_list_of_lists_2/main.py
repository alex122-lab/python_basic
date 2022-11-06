nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def list_struct(struct):
	for sub_struct in struct:
		if type(sub_struct) == int:
			out_list.append(sub_struct)
		else:
			list_struct(sub_struct)
	return out_list

out_list = []
list_struct(nice_list)
print(out_list)

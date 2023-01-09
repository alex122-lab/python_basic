speakers_file = open('numbers.txt', 'r', encoding='utf-8')
sum_num = 0
for i_line in speakers_file:
    num_line = i_line.strip()
    if num_line !='':
        sum_num += int(num_line)
speakers_file.close()

count_file = open('answer.txt', 'w', encoding='utf-8')
count_file.write(str(sum_num))
count_file.close()









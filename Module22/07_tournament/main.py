def write_file(file_n, text_w):
    text_file = open(file_n, 'w', encoding='utf-8')
    text_file.write(text_w)
    text_file.close()

speakers_file = open('first_tour.txt', 'r', encoding='utf-8')
k = int(speakers_file.readline())

second_tour = []
for i_line in speakers_file:
    print(999, i_line)
    man = i_line.split()
    if man != [] and int(man[2]) > k:
        second_tour.append(man)
speakers_file.close()

second_tour.sort(key=lambda k: k[2], reverse=True)

text = ''
text += str(len(second_tour)) + '\n'
for num, man in enumerate(second_tour):
    text += str(num + 1) + ') ' + man[1][0] + '. ' + man[0] + ' ' + man[2] + '\n'

write_file('second_tour.txt', text)

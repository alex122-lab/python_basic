import os

folder = os.path.abspath(os.path.join('..'))

def gen_files_path(directory):
    for links, dirs, files in list(os.walk(directory)):
        for file in files:
            if file.endswith('.py'):
                yield links + '/' + file

def file_parser(path_to_file):
    line_count = 0
    with open(path_to_file) as file:
        for line in file:
            if not line.isspace() and not line.startswith('#'):
                line_count += 1
                yield line_count

line_sum = 0
for file in gen_files_path(folder):
    line_sum_file = 0
    for number in file_parser(file):
        line_sum_file = number
    line_sum += line_sum_file
    print('Количество строк в файле:', file, '=', line_sum_file)

print('Общее количество строк во всех файлах =', line_sum)

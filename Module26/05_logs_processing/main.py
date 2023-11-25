import os

folder = os.path.abspath(os.path.join(''))

def error_log_generator(input_file_path: str):
    with open(input_file_path) as file:
        for line in file:
            if line.startswith('ERROR'):
                yield line

input_file_path = folder + '/data/work_logs.txt'
output_file_path = folder + '/data/output.txt'

with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")
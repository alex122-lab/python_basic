import os

def file_sizes(path):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path):
        file_path = os.path.abspath(os.path.join(path, i_elem))
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1
        else:
            result = file_sizes(file_path)
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1
    return files_stat

path = os.path.abspath(os.path.join('..', '..', 'Module22'))
result = file_sizes(path)

print(path)
print('Размер каталога (в Кб):', result[0] / 1024)
print('Количество подкаталогов:', result[2])
print('Количество файлов:', result[1])

import os

folder = os.path.abspath(os.path.join('..'))

def gen_files_path(directory):
    for links, dirs, files in list(os.walk(directory)):
        for file in files:
            yield links + '/' + file

for file in gen_files_path(folder):
   print(file)

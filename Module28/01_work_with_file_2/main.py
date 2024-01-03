class File:
    """
     Контекст-менеджер, который отвечает за открытие файла.
     При попытке открыть несуществующий файл менеджер автоматически
     создаёт и открывает этот файл в режиме записи.
     На выходе из менеджера подавляются все исключения,
     связанные с файлами.
     """
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding='UTF-8')
        except:
            self.file = open(self.filename, 'w', encoding='UTF-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

with File('doc.txt', 'r') as file:
    newfile = file.read()
    print(newfile)
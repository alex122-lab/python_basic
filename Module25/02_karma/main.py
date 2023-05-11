import random

class Karma:

    def __init__(self, __level_karma):
        self.__level_karma = __level_karma  # текущий уровень кармы

    def __str__(self):
        return 'Текущий уровень кармы: {}'.format(self.get_level_karma())

    def get_level_karma(self):
        return self.__level_karma

    def set_level_karma(self, __level_karma): # изменение уровеня кармы
        self.__level_karma = __level_karma

def one_day():
    num_ran = random.randint(1, 7)
    list_error = ['KillError','DrunkError','CarCrashError','GluttonyError','DepressionError']
    list_error_ran = random.sample(list_error,1)
    meaning = random.choices([num_ran, list_error_ran], weights=[10, 1])
    return meaning[0]

def write_file(name_file, text, action): # функция записи в файл
    with open(name_file, action) as f:
        f.write(text)

man_karma = Karma(0)
man_level_karma = man_karma.get_level_karma()

while man_level_karma < 500:
    try:
        day = one_day()
        man_level_karma += day
        man_karma.set_level_karma(man_level_karma)
    except TypeError:
        text = day[0] + '\n'
        write_file('karma.log', text, 'w')

print(man_karma)
def num_field(line, num): # функция проверки количество полей
    if len(line) == num:
        return True

def only_letters(word): # функция проверки наличия только букв.
    count_letter = 0
    for sym in word:
        if sym.isalpha():
            count_letter += 1
    if count_letter == len(word):
        return True

def is_mail(mail): # функция проверки почты
    if mail.find('.') >= 0 and mail.find('@') >= 0:
        return True

def range_age(num_age): # функция проверки диапазона возраста
    if str(num_age).isdigit():
        if (10 < int(num_age) <= 99):
            return True

def write_file(name_file, variable_name_file, text, action): # функция записи в файл
    with open(name_file, action) as variable_name_file:
        variable_name_file.write(text)

with open('registrations.txt', 'r') as registrations:
    for i_line in registrations:
        list_field = i_line.split()
        try:
            if num_field(list_field, 3):
                name, mail, age = list_field
                if not only_letters(name):
                    raise NameError
                elif not is_mail(mail):
                    raise SyntaxError
                elif not range_age(age):
                    raise ValueError
                else:
                    write_file('registrations_good.log', 'registrations_good', i_line, 'a')
            else:
                raise IndexError

        except IndexError:
            error_text = '.' * 20 + ' ' * 20 + 'НЕ присутствуют все три поля' + '\n'
            write_file('registrations_bed.log', 'registrations_bed', error_text, 'a')
        except NameError:
            error_text = i_line.replace('\n', ' ' * 20) + 'Поле «Имя» содержит НЕ только буквы'+ '\n'
            write_file('registrations_bed.log', 'registrations_bed', error_text, 'a')
        except SyntaxError:
            error_text = i_line.replace('\n', ' ' * 20) + 'Поле «Имейл» НЕ содержит @ и . (точку)'+ '\n'
            write_file('registrations_bed.log', 'registrations_bed', error_text, 'a')
        except ValueError:
            error_text = i_line.replace('\n', ' ' * 20) + 'Поле «Возраст» НЕ является числом от 10 до 99'+ '\n'
            write_file('registrations_bed.log', 'registrations_bed', error_text, 'a')

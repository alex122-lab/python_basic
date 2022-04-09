students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    list_st = (i, students[i]['age'])
    pairs.append(list_st)

print('Список пар "ID студента - Возраст":', pairs)

my_lst = f(students)[0]
len_sername = f(students)[1]
print('Полный список интересов всех студентов:', set(my_lst))
print('Общая длина всех фамилий студентов:', len_sername)

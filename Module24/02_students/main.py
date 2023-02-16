class Student:
    def __init__(self, full_name, num_group, grade):
        self.full_name = full_name
        self.num_group = num_group
        self.grade = grade

    def average_score(self):
        return sum(map(int, self.grade)) / len(self.grade)

students = []
for i in range(10):
    full_name = input('Введите фамилию и имя студента: ')
    num_group = input('Введите номер группы: ')
    grade = input('Введите оценки по 5 предметам через пробел: ').split()
    students.append(Student(full_name, num_group, grade))

sorted_student = sorted(students, key=lambda Student: Student.full_name)
sorted_students = sorted(sorted_student, key=lambda Student: Student.average_score())

print()
for i in range(10):
    print(sorted_students[i].full_name, '- средний балл', sorted_students[i].average_score())



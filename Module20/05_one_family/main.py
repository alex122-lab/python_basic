dict_famaly = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Анна"): 34,
    ("Сидоров", "Павел"): 10
}
famaly = input('Введите фамилию: ').lower()
print()
for fam, age in dict_famaly.items():
    men = fam[0].lower()
    if (famaly == men) or (famaly + 'а' == men) or (famaly == men + 'а'):
        print(fam[0], fam[1], age)


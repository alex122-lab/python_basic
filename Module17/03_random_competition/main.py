import random

first_team = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
second_team = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
winners = [first_team[num] if first_team[num] >= second_team[num] else second_team[num] for num in range(20)]
print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победители тура: ', winners)

# зачёт!

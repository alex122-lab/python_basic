class Personal:
    def __init__(self, __name, __surname, __age):
        self.__name = __name
        self.__surname = __surname
        self.__age = __age

    def __str__(self):
        return '{} {} {} лет: '.format(self.__name, self.__surname, self.__age)

class Employee(Personal):
    tax_salary = 0

    def calculate_salary(self):
        salary = self.tax_salary
        return salary

    def __str__(self):
        text = f'заработанная плата {self.calculate_salary():.2f} рублей'
        info = super().__str__() + text

        return info

class Manager(Employee):
    tax_salary = 13000

class Agent(Employee):
    tax_salary = 5000
    percent = 0.2

    def __init__(self, __name, __surname, __age, sales_volume):
        super().__init__(__name, __surname, __age)
        self.sales_volume = sales_volume

    def calculate_salary(self):
        salary = self.tax_salary + self.sales_volume * self.percent
        return salary

class Worker(Employee):

    def __init__(self, __name, __surname, __age, hours):
        super().__init__(__name, __surname, __age)
        self.hours = hours

    def calculate_salary(self):
        salary = 100 * self.hours
        return salary

manager_1 = Manager('Иван','Петров',38)
manager_2 = Manager('Алексей','Ветров',25)
manager_3 = Manager('Олег','Митин',58)

agent_1 = Agent('Виталий','Сидоров',32,100000)
agent_2 = Agent('Евгений','Захаров',42,90000)
agent_3 = Agent('Михаил','Зорин',25,110000)

worker_1 = Worker('Сергей','Зверев',45,268)
worker_2 = Worker('Петр','Александров',35,307)
worker_3 = Worker('Эдуард','Павлов',55,170)

print(manager_1)
print(manager_2)
print(manager_3)
print('-' * 60)
print(agent_1)
print(agent_2)
print(agent_3)
print('-' * 60)
print(worker_1)
print(worker_2)
print(worker_3)



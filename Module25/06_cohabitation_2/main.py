class House:
    """
    Базовый класс, описывающий дом
    Attributes:
       money_nightstand (int): количеством денег в тумбочке
        food_fridge (int): количеством еды в холодильнике
        cat_food (int): количество еды для кота
        dirt (int): количеством грязи
        count_fur_coat (int): сколько куплено шуб
        count_money (int): сколько заработано денег
        count_food (int): сколько съедено еды
    """
    money_nightstand = 100
    food_fridge = 50
    cat_food = 30
    dirt = 0
    count_fur_coat = 0
    count_money = 0
    count_food = 0

    def __str__(self):
        return f'Заработано денег {self.count_money}, съедено еды {self.count_food}, куплено шуб {self.count_fur_coat}'

class Residents_of_the_house(House):
    """
    Класс Житель дома. Родитель: House

    Args:
        name(str): передается имя человека или животного

    Attributes:
        money_nightstand (int): количеством денег в тумбочке
        food_fridge (int): количеством еды в холодильнике
        cat_food (int): количество еды для кота
        dirt (int): количеством грязи
        count_fur_coat (int): сколько куплено шуб
        count_money (int): сколько заработано денег
        count_food (int): сколько съедено еды
        degree_satiety (int): степень сытости
        """
    degree_satiety = 30

    def __init__(self,name):
        self.__name = name

    def get_name(self):
        """
        Геттер для получения имени
        :return: __name
        :rtype: string
        """
        return self.__name

    def set_name(self):
        """
        Сеттер для изменения имени
        :param name: имя
        :rtype: int
        """

    def __str__(self):
        return f'{self.__name}: степень сытости {self.degree_satiety}'

class People(Residents_of_the_house):
    """
    Класс Человек. Родитель: Residents_of_the_house

    Args:
        name(str): передается имя

    Attributes:
        money_nightstand (int): количеством денег в тумбочке
        food_fridge (int): количеством еды в холодильнике
        cat_food (int): количество еды для кота
        dirt (int): количеством грязи
        count_fur_coat (int): сколько куплено шуб
        count_money (int): сколько заработано денег
        count_food (int): сколько съедено еды
        degree_satiety (int): степень сытости
        degree_happiness (int): степень счастья
        portion_food (int): максимальное количество еды, съедаемой в день
    """
    degree_happiness = 100
    portion_food = 30

    def __str__(self):
        info_residents = super().__str__()
        info_people = f' степень счастья {self.degree_happiness}'
        info = ''.join((info_residents, ',', info_people))
        return info

    def eat(self):
        if House.food_fridge > self.portion_food:
            House.food_fridge -= self.portion_food
            self.degree_satiety += self.portion_food
            House.count_food += self.portion_food
        else:
            self.degree_satiety += House.food_fridge
            House.count_food += House.food_fridge
            House.food_fridge = 0

    def petting_the_cat(self):
        self.degree_happiness += 5
        self.degree_satiety -= 10

class Hasband(People):
    """
        Класс Муж. Родитель: People

        Args:
            name(str): передается имя

        Attributes:
            money_nightstand (int): количеством денег в тумбочке
            food_fridge (int): количеством еды в холодильнике
            cat_food (int): количество еды для кота
            dirt (int): количеством грязи
            count_fur_coat (int): сколько куплено шуб
            count_money (int): сколько заработано денег
            count_food (int): сколько съедено еды
            degree_satiety (int): степень сытости
            degree_happiness (int): степень счастья
            portion_food (int): максимальное количество еды, съедаемой в день
        """
    def act(self):
        if self.degree_satiety < 30:
           self.eat()
        elif 30 <= self.degree_satiety <= 60:
            self.work()
        elif degree_happiness < 20:
            self.play()
        else:
            self.petting_the_cat()

    def play(self):
        self.degree_satiety -= 10
        self.degree_happiness += 20

    def work(self):
        self.degree_satiety -= 10
        House.count_money += 150
        House.money_nightstand += 150

class Kid(People):
    """
        Класс Ребенок. Родитель: People

        Args:
            name(str): передается имя

        Attributes:
            money_nightstand (int): количеством денег в тумбочке
            food_fridge (int): количеством еды в холодильнике
            cat_food (int): количество еды для кота
            dirt (int): количеством грязи
            count_fur_coat (int): сколько куплено шуб
            count_money (int): сколько заработано денег
            count_food (int): сколько съедено еды
            degree_satiety (int): степень сытости
            degree_happiness (int): степень счастья
            portion_food (int): максимальное количество еды, съедаемой в день
        """
    portion_food = 20

    def act(self):
        if self.degree_satiety < 30:
           self.eat()

        elif self.degree_happiness < 20:
            self.play()
        else:
            self.petting_the_cat()

    def play(self):
        self.degree_satiety -= 10
        self.degree_happiness += 20

class Wife(People):
    """
        Класс Жена. Родитель: People

        Args:
            name(str): передается имя

        Attributes:
            money_nightstand (int): количеством денег в тумбочке
            food_fridge (int): количеством еды в холодильнике
            cat_food (int): количество еды для кота
            dirt (int): количеством грязи
            count_fur_coat (int): сколько куплено шуб
            count_money (int): сколько заработано денег
            count_food (int): сколько съедено еды
            degree_satiety (int): степень сытости
            degree_happiness (int): степень счастья
            portion_food (int): максимальное количество еды, съедаемой в день
        """
    def act (self):
        if self.degree_satiety < 30:
           self.eat()
        elif House.dirt > 80:
            self.сlean_house()
        elif House.money_nightstand >= 24000:
            self.bay_fur_coat()
        elif 30 <= self.degree_satiety <= 60:
            self.bay_products()
        else:
            self.petting_the_cat()

    def bay_products(self):
        self.degree_satiety -= 10
        if House.money_nightstand >= 80:
            House.money_nightstand -= 80
            House.food_fridge += 50
            House.cat_food += 30
        elif 40 < House.money_nightstand < 80:
            House.money_nightstand -= 40
            House.food_fridge += 30
            House.cat_food += 10
        else:
            House.food_fridge += House.money_nightstand
            House.money_nightstand = 0

    def bay_fur_coat(self):
        self.degree_satiety -= 10
        House.money_nightstand -= 350
        House.count_fur_coat += 1
        self.degree_happiness += 60

    def сlean_house(self):
        self.degree_satiety -= 10
        if House.dirt > 100:
            House.dirt -= 100
        else:
            House.dirt = 0

class Cat(Residents_of_the_house):
    """
        Класс Кот. Родитель: Residents_of_the_house

        Args:
            name(str): передается имя

        Attributes:
            money_nightstand (int): количеством денег в тумбочке
            food_fridge (int): количеством еды в холодильнике
            cat_food (int): количество еды для кота
            dirt (int): количеством грязи
            count_fur_coat (int): сколько куплено шуб
            count_money (int): сколько заработано денег
            count_food (int): сколько съедено еды
            degree_satiety (int): степень сытости
            portion_food (int): максимальное количество еды, съедаемой в день
        """
    portion_food = 10

    def __str__(self):
        info_residents = super().__str__()
        info_cat = f'Кот '
        info = ''.join((info_cat, info_residents))
        return info

    def act (self):
        if self.degree_satiety < 30:
           self.eat()
        elif 30 <= self.degree_satiety <= 60:
            self.tear_up_the_wallpaper()
        else:
            self.sleep()

    def eat(self):
        if House.cat_food > self.portion_food:
            House.cat_food -= self.portion_food
            self.count_food += self.portion_food
            self.degree_satiety += self.portion_food * 2
        else:
            self.degree_satiety += self.food_fridge
            self.count_food += self.food_fridge
            self.food_fridge = 0

    def sleep(self):
        self.degree_satiety -= 10

    def tear_up_the_wallpaper(self):
        self.degree_satiety -= 10
        House.dirt += 5

house_1 = House()
hasband_1 = Hasband('Иван')
wife_1 = Wife('Ирина')
kid_1 = Kid(People)
cat_1 = Cat('Барсик')
cat_2 = Cat('Мурзик')
cat_3 = Cat('Дымок')

list_people = [hasband_1, wife_1, kid_1]
list_cat = [cat_1, cat_2, cat_3]

for i in range(365):
    for people in list_people:
        if people.degree_satiety < 0 or people.degree_happiness < 10:
            list_people.remove(people)
        elif House.dirt > 90:
            people.degree_happiness -= 10
        people.act()

    for cat in list_cat:
        if cat.degree_satiety < 0:
            list_cat.remove(cat)
        else:
            cat.act()
    House.dirt += 5

print(house_1)

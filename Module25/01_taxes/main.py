class Property:
    tax_rate = 1/100  # ставка налога

    def __init__(self,worth):
        self.__worth = worth # стоимость единицы имущества

    def calculate_tax(self):
        tax = self.tax_rate * self.__worth
        return tax

    def get_worth(self):
        return self.__worth

class Apartment(Property):
    tax_rate = 1/1000

    def __str__(self):
        return 'Налог на квартиру: {tax:.2f} рублей'.format(worth=self.get_worth(), tax=self.calculate_tax())

class Car(Property):
    tax_rate = 1/200

    def __str__(self):
        return 'Налог на машину: {tax:.2f} рублей'.format(worth=self.get_worth(), tax=self.calculate_tax())

class CountryHouse(Property):
    tax_rate = 1 / 500

    def __str__(self):
        return 'Налог на дачу: {tax:.2f} рублей'.format(worth=self.get_worth(), tax=self.calculate_tax())

name_user = input('Введите свое имя: ')
user_money = int(input('Введите сколько у Вас денег (рублей): '))
cost_flat = int(input('Введите стоимость квартиры: '))
cost_car = int(input('Введите стоимость машины: '))
cost_country_house = int(input('Введите стоимость дачи: '))

user_flat = Apartment(cost_flat)
user_car = Car(cost_car)
user_country_house = CountryHouse(cost_country_house)
all_nalog = user_flat.calculate_tax() + user_car.calculate_tax() + user_country_house.calculate_tax()

print()
print(user_flat)
print(user_car)
print(user_country_house,'\n')

if user_money < all_nalog:
    delta = all_nalog - user_money
    print(f'У Вас недостаточно денег для уплаты всех налогов, не хватает {delta:.2f}', 'рублей.' )
else:
    print('У Вас достаточно денег для уплаты всех налогов')




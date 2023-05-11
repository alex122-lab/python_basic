import math
import random

class Car:
    count = 0
    def __init__(self,x,y, angle):
        self.x=x
        self.y=y
        self.angle = angle
        self.count += 1

    def __str__(self):
        return f'Текущие координаты: x= {round(self.x,2)}, y= {round(self.y,2)}, направление движения: {round(self.angle,2)} градусов'

    def move(self, distance):
        self.distance=distance
        radian = self.angle * math.pi / 180
        self.y += distance * math.sin(radian)
        self.x += distance * math.cos(radian)

    def rotate_car (self,rotate):
        self.rotate=rotate
        self.angle += self.rotate

class Bus(Car):
    count_passenger = 0
    max_passenger = 50
    many = 0
    info=''
    num_bus=0

    def __str__(self):
        info_car = super().__str__()
        info_bus = f'\nВ автобусе № {self.count} количество пассажиров: {self.count_passenger}, сумма денег: {round(self.many,2)}\n'
        info = ''.join((info_bus,info_car))
        return info

    def move(self, distance):
        super().move(distance)
        self.many += self.count_passenger * self.distance * 0.123

    def enter(self):
        enter_pass = random.randint(0,self.max_passenger)
        if self.count_passenger == self.max_passenger:
            print('Cвободных мест нет')
        elif self.count_passenger + enter_pass > self.max_passenger:
            self.count_passenger = self.max_passenger
        else:
            self.count_passenger = self.count_passenger + enter_pass

    def exit (self):
        exit_pass = random.randint(0, self.max_passenger)
        if self.count_passenger == 0:
            print('В автобусе нет пассажиров')
        elif self.count_passenger - exit_pass <= 0:
            self.count_passenger = 0
        else:
            self.count_passenger = self.count_passenger - exit_pass

bus_1 = Bus(5,7,90)
bus_1.move(10.4)
print(bus_1)

bus_1.enter()
bus_1.enter()

bus_1.rotate_car(44)
print(bus_1)
bus_1.move(10)
bus_1.exit()

bus_1.rotate_car(44)
print(bus_1)

bus_1.rotate_car(-14)
bus_1.move(14)
print(bus_1)
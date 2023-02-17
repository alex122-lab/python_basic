class Potate:
    states = {0: 'отсутствует', 1: 'росток', 2: 'зеленая', 3: 'зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
            # print(self.state)
        self.print_state()

    def print_state(self):
        print(f'картошка {self.index} сейчас {self.states[self.state]}')

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

class PotateGaden:
    def __init__(self, count):
        self.potatoes = [Potate(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potate in self.potatoes:
            i_potate.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('\nКартошка еще не созрела\n')
                break
                # return False
        else:
            print('Вся картошка созрела, можно собирать\n')
            return True

class Gardener:

    def __init__(self, name, gaden):
        self.name = name
        self.gaden = gaden
        self.collected_potateos = []


    def gardener_info(self): # садовник
        print(f'Садовник {self.name} собрал урожай картошки\n'
              f'Сколько собрал картошки: {len(self.collected_potateos)}')

    def take_care(self): # ухаживает
        print(f'Садовник {self.name} ухаживает за грядкой\n')
        self.gaden.grow_all()

    def harvesting(self): # собирает урожай
        for i_potate in self.gaden.potatoes:
            self.collected_potateos.append(i_potate)
        print(f'Садовник {self.name} собирает урожай\n')

garden = PotateGaden(5)
worker = Gardener('Сидоров Иван Ильич', garden)

while not garden.are_all_ripe():
    worker.take_care()
else:
    worker.harvesting()
    worker.gardener_info()









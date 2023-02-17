class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Land):
            return Dirt()

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Land):
            return Dust()

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Land):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()

class Land:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Land):
            return Lava()

class Storm:
    def __str__(self):
        return 'Шторм'

class Steam:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'

class Lightning:
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'

class Lava:
    def __str__(self):
        return 'Лава'

water = Water()
air = Air()
fire = Fire()
land = Land()

print(water + air)
print(water + fire)
print(water + land)
print(air + fire)
print(air + land)
print(fire + land)


from animals import Animal
from movements import Slither

class Snake(Animal, Slither):
    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, shift, food)
        Slither.__init__(self)
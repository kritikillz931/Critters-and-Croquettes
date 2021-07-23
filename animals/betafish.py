from animals import Animal
from movements import Swimming

class Betafish(Animal, Swimming):
    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, shift, food)
        Swimming.__init__(self)
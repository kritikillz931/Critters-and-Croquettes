from animals import Animal
from movements import Walking

class Horse(Animal, Walking):
    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, shift, food)
        Walking.__init__(self)
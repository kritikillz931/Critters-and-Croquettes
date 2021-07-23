from animals import Animal

class Horse(Animal):
    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, shift, food)
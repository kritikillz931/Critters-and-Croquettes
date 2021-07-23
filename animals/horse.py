from animals import Animal

class Horse(Animal):
    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
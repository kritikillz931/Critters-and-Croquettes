from animals import Animal
class Camel(Animal):
    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, shift, food)
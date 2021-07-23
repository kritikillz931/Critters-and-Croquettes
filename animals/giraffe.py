from animals import Animal
class Giraffe(Animal):
    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, shift, food)
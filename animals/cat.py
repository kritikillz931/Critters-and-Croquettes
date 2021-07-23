from animals import Animal
class Cat(Animal):
    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
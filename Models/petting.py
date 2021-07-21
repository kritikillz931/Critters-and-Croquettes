from datetime import date

class pettingAreaAnimal:

    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.dateAdded = date.today()


Johnny = pettingAreaAnimal("1", "Johnny", "Horse")
Diego = pettingAreaAnimal("2", "Diego", "Camel")
Milo = pettingAreaAnimal("3", "Milo", "Monkey")
Joe = pettingAreaAnimal("4", "Joe", "Elephant")
Snoop = pettingAreaAnimal("5", "Snoop", "Cat")

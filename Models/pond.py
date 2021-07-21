from datetime import date

class pondAreaAnimal:

    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.dateAdded = date.today()

Nemo = pondAreaAnimal("1", "Nemo", "Clownfish")
Ben = pondAreaAnimal("2", "Ben", "Shark")
Scott = pondAreaAnimal("3", "Scott", "Goldfish")
Sean = pondAreaAnimal("4", "Sean", "Betafish")
Larry = pondAreaAnimal("5", "Larry", "Angler fish")
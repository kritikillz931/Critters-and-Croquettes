from datetime import date

class pondAreaAnimal:

    def __init__(self, id, name, species, shift):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.dateAdded = date.today()
        self.shift = shift

Nemo = pondAreaAnimal("1", "Nemo", "Clownfish", "Morning")
Ben = pondAreaAnimal("2", "Ben", "Shark", "Morning")
Scott = pondAreaAnimal("3", "Scott", "Goldfish", "Morning")
Sean = pondAreaAnimal("4", "Sean", "Betafish", "Morning")
Larry = pondAreaAnimal("5", "Larry", "Angler fish", "Morning")

print(f'{Nemo.name} the {Nemo.species} is available to view during the {Nemo.shift} shift')
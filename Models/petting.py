from datetime import date

class pettingAreaAnimal:

    def __init__(self, id, name, species, shift):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.dateAdded = date.today()
        self.shift = shift


Johnny = pettingAreaAnimal("1", "Johnny", "Horse", "Midday")
Diego = pettingAreaAnimal("2", "Diego", "Camel", "Midday")
Milo = pettingAreaAnimal("3", "Milo", "Monkey", "Midday")
Joe = pettingAreaAnimal("4", "Joe", "Elephant", "Midday")
Snoop = pettingAreaAnimal("5", "Snoop", "Cat", "Midday")

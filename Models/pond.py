from datetime import date

class pondAreaAnimal:

    def __init__(self, id, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.swimming = True
        self.dateAdded = date.today()
        self.shift = shift
        self.food = food

         
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')



Nemo = pondAreaAnimal("1", "Nemo", "Clownfish", "Morning", "Fish food")
Ben = pondAreaAnimal("2", "Ben", "Shark", "Morning", "Fish food")
Scott = pondAreaAnimal("3", "Scott", "Goldfish", "Morning", "Fish food")
Sean = pondAreaAnimal("4", "Sean", "Betafish", "Morning", "Fish food")
Larry = pondAreaAnimal("5", "Larry", "Angler fish", "Morning", "Fish food")

print(Ben.feed())
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

         
    def __str__(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

class fishy_Fish:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

fishy_fish = fishy_Fish("Fishy Fish", "world famous variety of fish to feed")

Nemo = pondAreaAnimal("1", "Nemo", "Clownfish", "Morning", "Fish food")
Ben = pondAreaAnimal("2", "Ben", "Shark", "Morning", "Fish food")
Scott = pondAreaAnimal("3", "Scott", "Goldfish", "Morning", "Fish food")
Sean = pondAreaAnimal("4", "Sean", "Betafish", "Morning", "Fish food")
Larry = pondAreaAnimal("5", "Larry", "Angler fish", "Morning", "Fish food")

fishy_fish.animals.append(Nemo)
fishy_fish.animals.append(Ben)

print(f"{fishy_fish.attraction_name} is where you'll find animals such as")
for animal in fishy_fish.animals:
    print(f"""  * {animal.name} the {animal.species}""")
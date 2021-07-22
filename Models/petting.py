from datetime import date


class pettingAreaAnimal:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.dateAdded = date.today()
        self.shift = shift
        self.food = food

    def __str__(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

petty_pets = PettingZoo("Petty Pets", "world famous variety of animals to pet and feed")
        
Johnny = pettingAreaAnimal("Johnny", "Horse", "Midday", "Hay")
Diego = pettingAreaAnimal("Diego", "Camel", "Midday", "Grains")
Milo = pettingAreaAnimal("Milo", "Monkey", "Midday", "Banana")
Joe = pettingAreaAnimal("Joe", "Elephant", "Midday", "Roots" )
Snoop = pettingAreaAnimal("Snoop", "Cat", "Midday", "Everything")
Andrew = pettingAreaAnimal("Andrew", "Giraffe", "Midday", "Leaves")

petty_pets.animals.append(Johnny)
petty_pets.animals.append(Diego)
print(f"{petty_pets.attraction_name} is where you'll find animals such as")
for animal in petty_pets.animals:
    print(f"""  * {animal.name} the {animal.species}""")
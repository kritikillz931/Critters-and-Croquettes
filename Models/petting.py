from datetime import date

class pettingAreaAnimal:

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

Johnny = pettingAreaAnimal("1", "Johnny", "Horse", "Midday", "Hay")
Diego = pettingAreaAnimal("2", "Diego", "Camel", "Midday", "Grains")
Milo = pettingAreaAnimal("3", "Milo", "Monkey", "Midday", "Banana")
Joe = pettingAreaAnimal("4", "Joe", "Elephant", "Midday", "Roots" )
Snoop = pettingAreaAnimal("5", "Snoop", "Cat", "Midday", "Everything")

print(Johnny)
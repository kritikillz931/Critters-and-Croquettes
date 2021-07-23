from datetime import date
class Animal:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.dateAdded = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
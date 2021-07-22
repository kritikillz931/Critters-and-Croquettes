from datetime import date

class GlassTankAreaAnimal:

    def __init__(self, id, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.slithering = True
        self.dateAdded = date.today()
        self.shift = shift
        self.food = food

    def __str__(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

class snakey_Snakes:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

snakey_snakes = snakey_Snakes("Snakey Snakes", "world famous variety of snakes to feed")


Patrick = GlassTankAreaAnimal("1", "Patrick", "Python", "Evening", "Mice")
Kobe = GlassTankAreaAnimal("2", "Kobe", "Mamba", "Evening", "Mice")
Satan = GlassTankAreaAnimal("3", "Satan", "Garden Snake", "Evening", "Mice")
Dakota = GlassTankAreaAnimal("4", "Dakota", "Anaconda", "Evening", "Mice")
Richard = GlassTankAreaAnimal("5", "Richard", "Viper", "Evening", "Mice")

snakey_snakes.animals.append(Patrick)
snakey_snakes.animals.append(Kobe)

print(f"{snakey_snakes.attraction_name} is where you'll find animals such as")
for animal in snakey_snakes.animals:
    print(f"""  * {animal.name} the {animal.species}""")
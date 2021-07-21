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

Patrick = GlassTankAreaAnimal("1", "Patrick", "Python", "Evening", "Mice")
Kobe = GlassTankAreaAnimal("2", "Kobe", "Mamba", "Evening", "Mice")
Satan = GlassTankAreaAnimal("3", "Satan", "Garden Snake", "Evening", "Mice")
Dakota = GlassTankAreaAnimal("4", "Dakota", "Anaconda", "Evening", "Mice")
Richard = GlassTankAreaAnimal("5", "Richard", "Viper", "Evening", "Mice")

print(Patrick)
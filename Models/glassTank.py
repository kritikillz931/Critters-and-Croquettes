from datetime import date

class GlassTankAreaAnimal:

    def __init__(self, id, name, species, shift):
        self.id = id
        self.name = name
        self.species = species
        self.slithering = True
        self.dateAdded = date.today()
        self.shift = shift


Patrick = GlassTankAreaAnimal("1", "Patrick", "Python", "Evening")
Kobe = GlassTankAreaAnimal("2", "Kobe", "Mamba", "Evening")
Satan = GlassTankAreaAnimal("3", "Satan", "Garden Snake", "Evening")
Dakota = GlassTankAreaAnimal("4", "Dakota", "Anaconda", "Evening")
Richard = GlassTankAreaAnimal("5", "Richard", "Viper", "Evening")


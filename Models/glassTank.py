from datetime import date

class GlassTankAreaAnimal:

    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.slithering = True
        self.dateAdded = date.today()


Patrick = GlassTankAreaAnimal("1", "Patrick", "Python")
Kobe = GlassTankAreaAnimal("2", "Kobe", "Mamba")
Satan = GlassTankAreaAnimal("3", "Satan", "Garden Snake")
Dakota = GlassTankAreaAnimal("4", "Dakota", "Anaconda")
Richard = GlassTankAreaAnimal("5", "Richard", "Viper")


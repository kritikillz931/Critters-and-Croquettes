from datetime import date



    def __str__(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

Patrick = GlassTankAreaAnimal("1", "Patrick", "Python", "Evening", "Mice")
Kobe = GlassTankAreaAnimal("2", "Kobe", "Mamba", "Evening", "Mice")
Satan = GlassTankAreaAnimal("3", "Satan", "Garden Snake", "Evening", "Mice")
Dakota = GlassTankAreaAnimal("4", "Dakota", "Anaconda", "Evening", "Mice")
Richard = GlassTankAreaAnimal("5", "Richard", "Viper", "Evening", "Mice")


# snakey_snakes = snakey_Snakes("Snakey Snakes", "world famous variety of snakes to feed")

print(f"{snakey_snakes.attraction_name} is where you'll find animals such as")
for animal in snakey_snakes.animals:
    print(f"""  * {animal.name} the {animal.species}""")




# snakey_snakes = snakey_Snakes("Snakey Snakes", "world famous variety of snakes to feed")

print(f"{snakey_snakes.attraction_name} is where you'll find animals such as")
for animal in snakey_snakes.animals:
    print(f"""  * {animal.name} the {animal.species}""")
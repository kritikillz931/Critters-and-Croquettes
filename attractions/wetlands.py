from attractions import Attraction

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def addAnimal(self, animal):
            try:
                if animal.swimming_speed > -1:
                    self.animals.append(animal)
                    print(f"{animal} now lives in {self.name}")
            except AttributeError:
                 print(f'{animal} can\'t swim, so please do not put it in the {self.name} attraction.') 
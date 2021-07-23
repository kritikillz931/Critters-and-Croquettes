from . import attractions

class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()
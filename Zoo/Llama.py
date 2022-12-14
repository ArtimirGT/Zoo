from BaseAnimals import *
class llama(baseAnimal):
    def __init__(self, name, eating, age):
        super().__init__(name, eating, age)
        self._type = "llama"
        self._biome = "South America"
        self._area = 150
        self._food = ["grass"]
        self._GrassOrMeat = "travu est"
        self._sound = "HHHHH TFU!!!"
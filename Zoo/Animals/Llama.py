from BaseAnimals import *
class llama(baseAnimal):
    def __init__(self, name, eating, age):
        super().__init__(name, eating, age)
        self._type = "llama"
        self._biome = "desert"
        self._area = 10
        self._food = ["grass"]
        self._IsPredator = False
        self._sound = "HHHHH TFU!!!"
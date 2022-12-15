from BaseAnimals import *
class elephant(baseAnimal):
    def __init__(self, name, eating, age):
        super().__init__(name, eating, age)
        self._type = "elephant"
        self._biome = "desert"
        self._area = 50
        self._food = ["grass", "leafs"]
        self._IsPredator = False
        self._sound = "TUUUUUUUUUUUUUU"
from BaseAnimals import *
class wolf(baseAnimal):
    def __init__(self, name, eating, age):
        super().__init__(name, eating, age)
        self._type = "wolf"
        self._biome = "forest"
        self._area = 25
        self._food = ["rabbits", "humans"]
        self._IsPredator = True
        self._sound = "auf"
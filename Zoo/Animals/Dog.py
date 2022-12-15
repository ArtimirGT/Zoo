from BaseAnimals import *
class dog(baseAnimal):
    def __init__(self, name, eating, age):
        super().__init__(name, eating, age)
        self._type = "dog"
        self._biome = "anywhere"
        self._area = 50
        self._food = ["meat", "dog food"]
        self._IsPredator = True
        self._sound = "gav"
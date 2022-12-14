from BaseAnimals import *
class dog(baseAnimal):
    def __init__(self, name, eating, age):
        super().__init__(name, eating, age)
        self._type = "dog"
        self._biome = "anywhere"
        self._area = 1000
        self._food = ["meat", "dog food"]
        self._GrassOrMeat = "pradator"
        self._sound = "gav"
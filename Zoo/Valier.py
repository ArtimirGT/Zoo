from BaseAnimals import *

class valier:
    def __init__(self, name, size, biome):
        self.name = name
        self.size = size
        self.biome = biome
        self.animals = []
        self.IsPredator = False
        self.predatorType = ''
        self.__freeSize = size

    def add(self, animal):
        if animal.IsPredator == True and len(self.animals) == 0 and animal.area < self.__freeSize:
            self.IsPredator = True
            self.predatorType = animal.type
        if animal.IsPredator == self.IsPredator and animal.biome == self.biome and animal.area < self.__freeSize:
            if animal.IsPredator == True and animal.type == self.predatorType:
                self.animals.append(animal)
                self.__freeSize -= animal.area
                print("added", animal.type)
            elif animal.IsPredator == True:
                print("нельзя подселить", animal.type, "(" + animal.name + ")", ": несовместимые хищники")
            else:
                self.animals.append(animal)
                self.__freeSize -= animal.area
                print("added", animal.type)
        else:
            print("нельзя подселить", animal.type, "(" + animal.name + ")", ": неверный биом или несовместимые виды")

    def printAnimalList(self):
        print("--- animal list:", self.name, "---")
        for i in self.animals:
            print(i.name, "(" + i.type + ")")
        print("---------------------")

    @property
    def freeSize(self):
        return self.__freeSize
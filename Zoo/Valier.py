from BaseAnimals import *

class valier:
    def __init__(self, name, size, biome: str):
        self.name = name
        self.size = size
        self.biome = biome
        self.animals = []
        self.IsPredator = False
        self.predatorType = ''
        self.__freeSize = size

    def add(self, animal):
        if animal.IsPredator == True and len(self.animals) == 0 and animal.area <= self.__freeSize:
            self.IsPredator = True
            self.predatorType = animal.type
        if animal.IsPredator == self.IsPredator and (animal.biome == self.biome or animal.biome == "anywhere") and animal.area <= self.__freeSize:
            if animal.IsPredator == True and animal.type == self.predatorType:
                self.animals.append(animal)
                self.__freeSize -= animal.area
                print(self.name, ": added", animal.type)
            elif animal.IsPredator == True:
                print("нельзя подселить", animal.type, "(" + animal.name + ")", ": несовместимые хищники")
            else:
                self.animals.append(animal)
                self.__freeSize -= animal.area
                print(self.name, ": added", animal.type)
        else:
            print("нельзя подселить", animal.type, "(" + animal.name + ")", ": неверный биом, несовместимые виды или не хватает места")
    def printAnimalList(self):
        print("")
        print("--- animal list:", self.name, "---")
        for i in self.animals:
            print(i.name, "(" + i.type + ")")
        print("---------------------")

    def delete(self, name):
        self.animals.remove(name)
        print(self.name, ": deleted", name.name, "(" + name.type + ")")
        self.__freeSize += name.area

    def allDoSound(self):
        print("")
        print("--- animals :", self.name + "; do sound ---")
        for i in self.animals:
            i.doSound()
        print("---------------------")

    def feed(self,value, food):
        print("")
        print("--- animals :", self.name + "; eating ---")
        for i in self.animals:
            i.eat((value / len(self.animals)), food)
        print("---------------------")

    def getWhoNotFeeded(self):
        print("")
        print("---", self.name, ": not feeded ---")
        for i in self.animals:
            if i.IsFeeded == False:
                print(i.name, "(" + i.type + "); need:", i.food, "; this much:", i._eating - i.sum)
        print("---------------------")
    @property
    def freeSize(self):
        return self.__freeSize
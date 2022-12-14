class baseAnimal:
    def __init__(self, name, eating, age):
        self.name = name
        self._eating = eating
        self._age = age
        self._type = ""
        self._biome = ""
        self._area = 0
        self._food = ""
        self._GrassOrMeat = ""
        self._sound = ""
        self.IsFeeded = False
        self.sum = 0

    def eat(self, food):
        if self.sum + food >= self._eating:
            self.IsFeeded = True
        else:
            self.sum = self.sum + food

    def doSound(self):
        print(self._type + ": " + self._sound)

    def play(self):
        print(self._type + " играет")

    @property
    def type(self):
        return self._type

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value
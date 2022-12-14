class baseAnimal:
    def __init__(self, name, eating, age):
        self.name = name
        self._eating = eating
        self._age = age
        self._type = ""
        self._biome = ""
        self._area = 0
        self._food = []
        self._IsPredator = bool
        self._sound = ""
        self.IsFeeded = False
        self.sum = 0

    def eat(self, value, food):
        if self.sum + value >= self._eating and food in self._food:
            print(self.name, ': я наелся')
            self.IsFeeded = True
        elif food in self._food:
            print(self.name, ': я не наелся')
            self.sum = self.sum + value
        else:
            print(self.name, ': я это не буду')

    def doSound(self):
        print(self.name, "(" + self._type + ")" + ": " + self._sound)

    def play(self):
        print(self._type + " играет")

    @property
    def type(self):
        return self._type

    @property
    def food(self):
        return self._food

    @property
    def area(self):
        return self._area

    @property
    def IsPredator(self):
        return self._IsPredator

    @property
    def biome(self):
        return self._biome

    @area.setter
    def area(self, value):
        if value >= 0:
            print(self.name, ": area set", value)
            self._area = value
        else:
            print("Ty durak?")
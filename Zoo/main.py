from Animals.Wolf import *
from Animals.Dog import *
from Animals.Llama import *
from Valier import *
V = valier("Wolfes", 1000, "forest")
V.add(wolf("Boris", 10, 6))
V.add(wolf("Anatoly", 10, 7))
V.add(llama("Kira Yoshikage", 5, 15))
V.add(dog("Maks", 4, 5))
V.printAnimalList()
print(V.freeSize)
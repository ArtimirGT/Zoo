from Animals.Wolf import *
from Animals.Dog import *
from Animals.Llama import *
from Animals.Elephant import *
from Valier import *
boris = wolf("Boris", 10, 6)
anatoly = wolf("Anatoly", 10, 7)
kira = llama("Kira Yoshikage", 5, 15)
du = elephant("Du", 20, 30)
maks = dog("Maks", 5, 4)
V = valier("Grass", 100, "desert")
V.add(kira)
V.add(du)
V.add(maks)
V.allDoSound()
V.feed(5, "grass")
V.getWhoNotFeeded()
V.feed(35, "leafs")
V.getWhoNotFeeded()
W = valier("Wolves", 100, "forest")
W.add(boris)
W.add(anatoly)
W.add(maks)
W.allDoSound()
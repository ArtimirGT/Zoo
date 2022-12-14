from Wolf import *
from Dog import *
from Llama import *
wolf = wolf("Boris", 10, 6)
dog = dog("Vasya", 5, 3)
llama = llama("Kira", 2, 10)
wolf.eat(9, "rabbits")
print(wolf.IsFeeded)
wolf.eat(1, "rabbits")
print(wolf.IsFeeded)
print('')
dog.area = -1
dog.area = 100
print(dog.area)
llama.doSound()
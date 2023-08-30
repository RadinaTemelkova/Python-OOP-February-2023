from project.animal import Animal
from project.reptile import Reptile
from project.mammal import Mammal
from project.lizard import Lizard
from project.snake import Snake
from project.bear import Bear
from project.gorilla import Gorilla


mammal = Mammal("Koko")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("Mickey")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

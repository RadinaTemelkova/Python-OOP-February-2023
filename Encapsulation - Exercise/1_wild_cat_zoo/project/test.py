from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo


zoo = Zoo("The Great Zoo", 3000, 5, 8)

animals = [Cheetah("Thomas", "Male", 3), Cheetah("Tea", "Female", 1), Lion("Leo", "Male", 2), Tiger("Tiger", "Male", 3), Tiger("Tigress", "Female", 1), Lion("Lea", "Female", 5)]

prices = [250, 195, 200, 179, 204, 190]

workers = [Keeper("Keeper_1", 29, 100), Keeper("Keeper_2", 29, 80), Keeper("Keeper_3", 41, 105), Caretaker("Caretaker_1", 21, 110), Caretaker("Caretaker_2", 39, 100), Caretaker("Caretaker_3", 40, 150), Vet("Vet_1", 44, 300), Vet("Vet_2", 22, 280), Vet("Vet_3", 21, 260)]

for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

for worker in workers:
    print(zoo.hire_worker(worker))

print(zoo.tend_animals())

print(zoo.pay_workers())

print(zoo.fire_worker("Keeper_2"))

print(zoo.animals_status())
print(zoo.workers_status())


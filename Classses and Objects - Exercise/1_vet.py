class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space > 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals and animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


person_1 = Vet("John")
person_2 = Vet("Johnathan")
print(person_1.register_animal("Tom"))
print(person_2.register_animal("Cloe"))
print(person_1.register_animal("Fifi"))
print(person_1.register_animal("Bobby"))
print(person_2.register_animal("Kara"))
print(person_2.unregister_animal("Cora"))
print(person_1.register_animal("Sally"))
print(person_1.unregister_animal("Fifi"))
print(person_1.unregister_animal("Tom"))
print(person_1.info())
print(person_2.info())

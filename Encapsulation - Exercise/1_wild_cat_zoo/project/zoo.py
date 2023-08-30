from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def not_enough_space(self, subject):
        return f"Not enough space for {subject}"

    def add_animal(self, animal: Animal, price: float) -> str:
        if len(self.animals) + 1 <= self.__animal_capacity:
            if self.__budget - price >= 0:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return self.not_enough_space("animal")

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) + 1 <= self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return self.not_enough_space("worker")

    def fire_worker(self, worker_name: str) -> str:
        worker_found = [w for w in self.workers if w.name == worker_name]
        if worker_found:
            self.workers.remove(worker_found[0])
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        sum_of_salaries = 0
        for worker in self.workers:
            sum_of_salaries += worker.salary

        if self.__budget - sum_of_salaries >= 0:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = 0
        for animal in self.animals:
            total_money_for_care += animal.money_for_care

        if self.__budget - total_money_for_care >= 0:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self) -> str:

        lions_data, tigers_data, cheetahs_data = [], [], []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions_data.append(str(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers_data.append(str(animal))
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs_data.append(str(animal))

        lions = "\n".join(lions_data)
        tigers = "\n".join(tigers_data)
        cheetahs = "\n".join(cheetahs_data)

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions_data)} Lions:\n" \
               f"{lions}\n" \
               f"----- {len(tigers_data)} Tigers:\n" \
               f"{tigers}\n" \
               f"----- {len(cheetahs_data)} Cheetahs:\n" \
               f"{cheetahs}"


    def workers_status(self) -> str:

        keepers_data, caretakers_data, vets_data = [], [], []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers_data.append(str(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretakers_data.append(str(worker))
            elif worker.__class__.__name__ == "Vet":
                vets_data.append(str(worker))

        keepers = "\n".join(keepers_data)
        caretakers = "\n".join(caretakers_data)
        vets = "\n".join(vets_data)

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers_data)} Keepers:\n" \
               f"{keepers}\n" \
               f"----- {len(caretakers_data)} Caretakers:\n" \
               f"{caretakers}\n" \
               f"----- {len(vets_data)} Vets:\n" \
               f"{vets}"












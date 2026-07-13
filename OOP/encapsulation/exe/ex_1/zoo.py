from project.lion import Lion

from project.tiger import Tiger

from project.cheetah import Cheetah

from project.keeper import Keeper

from project.caretaker import Caretaker

from project.vet import Vet


class Zoo:
    def __init__(self,name,budget,animal_capacity,workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self,worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self,worker_name):
       for worker in self.workers:
           if worker.name == worker_name:
               self.workers.remove(worker)
               return f"{worker_name} fired successfully"
       return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        pay_check = sum(worker.salary for worker in self.workers)
        if pay_check <= self.__budget:
            self.__budget -= pay_check
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"


    def tend_animals(self):
        money_to_tend = sum(animal.money_to_care for animal in self.animals)
        if money_to_tend <= self.__budget:
            self.__budget -= money_to_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        lines = [f"You have {len(self.animals)} animals",
                 f"----- {len(lions)} Lions:", *[repr(a) for a in lions],
                 f"----- {len(tigers)} Tigers:", *[repr(a) for a in tigers],
                 f"----- {len(cheetahs)} Cheetahs:", *[repr(a) for a in cheetahs]]
        return "\n".join(lines)

    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        lines = [f"You have {len(self.workers)} workers",
                 f"----- {len(keepers)} Keepers:", *[repr(w) for w in keepers],
                 f"----- {len(caretakers)} Caretakers:", *[repr(w) for w in caretakers],
                 f"----- {len(vets)} Vets:", *[repr(w) for w in vets]]
        return "\n".join(lines)

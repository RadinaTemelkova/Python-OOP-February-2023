from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    CONDITIONER_CONSUMPTION_PER_KM = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption_for_distance = distance * (self.fuel_consumption + self.CONDITIONER_CONSUMPTION_PER_KM)

        if self.fuel_quantity >= consumption_for_distance:
            self.fuel_quantity -= consumption_for_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_CONSUMPTION_PER_KM = 1.6
    FUEL_KEPT_AFTER_REFILL = 95 / 100

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption_for_distance = distance * (self.fuel_consumption + self.CONDITIONER_CONSUMPTION_PER_KM)

        if self.fuel_quantity >= consumption_for_distance:
            self.fuel_quantity -= consumption_for_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_KEPT_AFTER_REFILL



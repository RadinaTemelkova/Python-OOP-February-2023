from typing import List
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_match = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer_match = [c for c in self.customers if c.id == subscription_match.customer_id][0]
        trainer_match = [t for t in self.trainers if t.id == subscription_match.trainer_id][0]
        plan_match = [p for p in self.plans if p.id == subscription_match.exercise_id][0]
        equipment_match = [e for e in self.equipment if e.id == plan_match.equipment_id][0]

        return f"{subscription_match}\n"\
               f"{customer_match}\n"\
               f"{trainer_match}\n" \
               f"{equipment_match}\n"\
               f"{plan_match}\n"





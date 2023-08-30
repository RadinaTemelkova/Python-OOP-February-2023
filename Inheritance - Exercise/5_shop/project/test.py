from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

food = Food("salad")
drink = Drink("soft drink")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("soft drink"))
repo.find("salad").decrease(8)
print(repo)

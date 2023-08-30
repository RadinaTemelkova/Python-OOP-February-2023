from project.beverage.beverage import Beverage
from project.food.main_dish import MainDish
from project.product import Product

product_1 = Product("tea", 3.7)
print(product_1.__class__.__name__)
print(product_1.name)
print(product_1.price)
beverage_1 = Beverage("tea", 3.7, 50)
print(beverage_1.__class__.__name__)
print(beverage_1.__class__.__bases__[0].__name__)
print(beverage_1.name)
print(beverage_1.price)
print(beverage_1.milliliters)
lasagna = MainDish("lasagna", 19.90, 300)
print(lasagna.__class__.__name__)
print(lasagna.__class__.__bases__[0].__name__)
print(lasagna.name)
print(lasagna.price)
print(lasagna.grams)

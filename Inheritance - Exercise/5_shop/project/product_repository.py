from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product_found = [current_product for current_product in self.products if current_product.name == product_name]
        if product_found:
            return product_found[0]

    def remove(self, product_name: str):
        product_to_remove = self.find(product_name)

        if product_to_remove:
            self.products.remove(product_to_remove)

    def __repr__(self):
        return "\n".join([f"{p}: {p.quantity}" for p in self.products])


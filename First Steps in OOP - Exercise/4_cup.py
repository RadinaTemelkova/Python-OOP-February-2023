class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity_to_add):
        if self.size - self.quantity >= quantity_to_add:
            self.quantity += quantity_to_add

    def status(self):
        free_space_in_cup = self.size - self.quantity
        return free_space_in_cup


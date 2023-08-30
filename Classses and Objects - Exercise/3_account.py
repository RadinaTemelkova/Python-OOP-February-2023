class Account:
    def __init__(self, account_id: int, name: str, balance: int = 0):
        self.id = account_id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"



account = Account(1234, "John", 2000)
print(account.credit(600))
print(account.debit(1500))
print(account.info())


account = Account(5678, "Johnathan")
print(account.debit(700))
print(account.credit(2000))
print(account.debit(700))
print(account.info())

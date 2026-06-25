class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

account = BankAccount("Maria", 100)
print(account.deposit(50))    # Deposited 50. New balance: 150
print(account.withdraw(200))  # Insufficient funds
print(account.withdraw(100))  # Withdrew 100. New balance: 50
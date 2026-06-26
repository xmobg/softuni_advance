class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid amount"

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"

        elif amount < 0:
            return "Invalid amount"
        return "Insufficient funds"

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"

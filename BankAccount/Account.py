class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough balance")
        else:
            self.balance -= amount
            print("Withdraw successful")

    def __str__(self):
        return f"Account owner: {self.owner}\nBalance: {self.balance}"

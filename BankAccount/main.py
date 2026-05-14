from Account import Account

jose = Account("Jose", 200)
jose.deposit(200)
jose.withdraw(100)
jose.withdraw(400)
print(jose)

print(jose.owner)
print(jose.balance)



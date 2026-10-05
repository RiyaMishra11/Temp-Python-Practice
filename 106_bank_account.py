"""106 - Bank Account Simulator"""

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = float(balance)
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance

    def statement(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "transactions": self.transactions
        }

def main():
    account = BankAccount("Riya", 5000)
    account.deposit(1500)
    account.withdraw(1000)
    print(account.statement())

if __name__ == "__main__":
    main()

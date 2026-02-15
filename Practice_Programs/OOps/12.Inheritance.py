#12. Account and SavingsAccount

class Account:
    def __init__(self, balance):
        self.balance = balance
    def show_balance(self):
        print(f"Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance * self.interest_rate /100

acc = SavingsAccount(1000, 5)
acc.add_interest()
acc.show_balance()
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account {self.account_number}: Balance = ${self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Withdrawal exceeds overdraft limit.")

#example usage
savings = SavingsAccount(12345, 1000, 0.05)
checking = CheckingAccount(67890, 500, 200)

savings.deposit(500)
savings.apply_interest()
savings.display_balance()

checking.withdraw(600)
checking.display_balance()
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate_precentage, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate_precentage/100
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    def display_account_info(self):
        print(f"Balance is : {self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
# create first account
account1 = BankAccount(2, 500)
account1.deposit(100)
account1.deposit(200)
account1.deposit(300)
account1.withdraw(250)
account1.yield_interest()
account1.display_account_info()

# create second account
account2 = BankAccount(1)
account2.deposit(1000)
account2.deposit(500)
account2.withdraw(200)
account2.withdraw(300)
account2.withdraw(400)
account2.withdraw(200)
account2.yield_interest()
account2.display_account_info()

class BankAccount:
    accounts = []
    
    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            print(f"Interest rate: {account.int_rate_precantage}%, Balance: ${account.balance}")
        
    def __init__(self, int_rate_precantage, balance=0):
        self.balance = balance
        self.int_rate_precantage = int_rate_precantage
        BankAccount.accounts.append(self)
account1 = BankAccount(2, 500)
account2 = BankAccount(1, 1000)


BankAccount.print_accounts()
        